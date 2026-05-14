from flask import Flask, render_template, request, jsonify, send_file
import hashlib
import os
import mimetypes
from reportlab.pdfgen import canvas
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# =========================================================
# MALWARE DATABASE
# =========================================================
KNOWN_MALWARE_HASHES = {
    "44d88612fea8a8f36de82e1278abb02f": "EICAR Test Virus",
    "e3b0c44298fc1c149afbf4c8996fb924": "Empty File Suspicious Pattern"
}

# =========================================================
# HASH ENGINE
# =========================================================
def generate_hashes(filepath):
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    sha256 = hashlib.sha256()

    with open(filepath, "rb") as f:
        while chunk := f.read(4096):
            md5.update(chunk)
            sha1.update(chunk)
            sha256.update(chunk)

    return {
        "md5": md5.hexdigest(),
        "sha1": sha1.hexdigest(),
        "sha256": sha256.hexdigest()
    }

# =========================================================
# VIRUS CHECKER
# =========================================================
def virus_check(md5_hash):
    if md5_hash in KNOWN_MALWARE_HASHES:
        return f"🔴 MALWARE DETECTED: {KNOWN_MALWARE_HASHES[md5_hash]}"
    return "🟢 No known threats found"

# =========================================================
# RISK ENGINE
# =========================================================
def risk_score(filepath):
    score = 0

    size = os.path.getsize(filepath)
    ext = os.path.splitext(filepath)[1].lower()

    if size > 5_000_000:
        score += 40
    elif size > 1_000_000:
        score += 20

    if ext in [".exe", ".bat", ".cmd", ".sh", ".apk"]:
        score += 50

    if ext in [".zip", ".rar"]:
        score += 20

    return min(score, 100)

# =========================================================
# FILE CLASSIFICATION
# =========================================================
def classify(ext):
    if ext in [".exe", ".bat", ".cmd", ".sh"]:
        return "Executable (High Risk)"
    elif ext in [".pdf", ".docx", ".txt"]:
        return "Document"
    elif ext in [".jpg", ".jpeg", ".png"]:
        return "Image"
    return "Unknown"

# =========================================================
# DASHBOARD
# =========================================================
@app.route("/")
def dashboard():
    return render_template("dashboard.html")

# =========================================================
# FILE HASH SCANNER PAGE
# =========================================================
@app.route("/scanner", methods=["GET", "POST"])
def scanner():

    data = {}

    if request.method == "POST":

        file = request.files["file"]

        if file:

            path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(path)

            hashes = generate_hashes(path)

            data = {
                "hashes": hashes,
                "file_size": os.path.getsize(path),
                "file_type": mimetypes.guess_type(path)[0] or "Unknown",
                "risk": risk_score(path),
                "virus": virus_check(hashes["md5"]),
                "file_class": classify(os.path.splitext(path)[1].lower())
            }

    return render_template("index.html", **data)

# =========================================================
# TOOLS HUB
# =========================================================
@app.route("/tools")
def tools():
    return render_template("tools.html")

# =========================================================
# TXT → PDF
# =========================================================
@app.route("/txt-to-pdf", methods=["POST"])
def txt_to_pdf():

    file = request.files["file"]

    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    pdf_path = os.path.join(
        OUTPUT_FOLDER,
        file.filename + ".pdf"
    )

    c = canvas.Canvas(pdf_path)

    with open(path, "r", errors="ignore") as f:

        y = 800

        for line in f.readlines():

            c.drawString(50, y, line.strip()[:120])
            y -= 15

            if y < 50:
                c.showPage()
                y = 800

    c.save()

    return send_file(pdf_path, as_attachment=True)

# =========================================================
# IMAGE → PDF
# =========================================================
@app.route("/image-to-pdf", methods=["POST"])
def image_to_pdf():

    file = request.files["file"]

    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    image = Image.open(path)

    pdf_path = os.path.join(
        OUTPUT_FOLDER,
        file.filename + ".pdf"
    )

    if image.mode == "RGBA":
        image = image.convert("RGB")

    image.save(pdf_path, "PDF")

    return send_file(pdf_path, as_attachment=True)

# =========================================================
# IMAGE → TEXT (REAL OCR)
# =========================================================
@app.route("/image-to-text", methods=["POST"])
def image_to_text():
    file = request.files["file"]

    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    try:
        image = Image.open(path)
        extracted_text = pytesseract.image_to_string(image)

        return render_template(
        "ocr_result.html",
         extracted_text=extracted_text,
        filename=file.filename
        )

    except Exception as e:
        return jsonify({
            "error": "OCR failed",
            "message": str(e)
        })

# =========================================================
# API
# =========================================================
@app.route("/api/hash", methods=["POST"])
def api_hash():

    file = request.files["file"]

    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    return jsonify(generate_hashes(path))

# =========================================================
# RUN APPLICATION
# =========================================================
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )