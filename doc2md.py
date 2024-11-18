import os
import re
import unicodedata
from docx import Document


def slugify(text):
    """Chuyển đổi chuỗi thành dạng slug (viết thường, không dấu, nối bằng dấu gạch dưới)."""
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')
    text = re.sub(r'[^\w\s-]', '', text).strip().lower()
    return re.sub(r'[\s]+', '_', text)


def create_markdown_from_word(word_file, output_dir):
    # Đọc file Word
    doc = Document(word_file)

    # Tạo thư mục gốc
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Biến lưu thư mục hiện tại và cấp chỉ mục
    current_paths = {0: output_dir}

    # Duyệt qua các đoạn văn trong Word
    for paragraph in doc.paragraphs:
        text = paragraph.text.strip()
        if not text:
            continue

        # Phát hiện cấp chỉ mục (số đầu mục)
        match = re.match(r"^(\d+(\.\d+)*)\s+(.+)", text)
        if match:
            index = match.group(1)  # Chỉ mục (vd: 1, 1.1, 1.1.1)
            title = match.group(3)  # Tiêu đề (vd: Tải ứng dụng và cài đặt trên máy tính)
            level = len(index.split("."))  # Đếm số cấp dựa trên số lượng dấu '.'

            # Tạo thư mục tương ứng
            folder_name = f"s{index.replace('.', '')}"  # Định danh thư mục (vd: s1, s11)
            parent_path = current_paths.get(level - 1, output_dir)  # Lấy thư mục cha
            current_path = os.path.join(parent_path, folder_name)
            os.makedirs(current_path, exist_ok=True)
            current_paths[level] = current_path

            # Sinh file Markdown với tên phù hợp
            slug_title = slugify(title)  # Chuyển tiêu đề thành dạng slug
            md_file_name = f"{index.replace('.', '')}_{slug_title}.md"  # Tên file Markdown
            md_file_path = os.path.join(current_path, md_file_name)

            with open(md_file_path, "w", encoding="utf-8") as f:
                f.write(f"# {title}\n\n")  # Tiêu đề chính trong file Markdown
        else:
            # Ghi nội dung còn lại vào file Markdown hiện tại
            current_path = current_paths[max(current_paths.keys())]
            md_file = os.path.join(current_path, "content.md")
            with open(md_file, "a", encoding="utf-8") as f:
                f.write(text + "\n\n")

    # Xử lý ảnh
    for i, rel in enumerate(doc.inline_shapes):
        if rel.type == "PICTURE":
            # Lưu ảnh vào thư mục hiện tại
            img_path = os.path.join(current_paths[max(current_paths.keys())], f"image_{i}.png")
            with open(img_path, "wb") as f:
                f.write(rel._inline.graphic.graphicData.pic.blipFill.blip.embed.part.blob)


if __name__ == "__main__":
    word_file = "/Users/nguyenvanlam/sources/document/System/KidSafe/Guide/HD_cai_dat_va_su_dung_KidSafe_v2.0.docx"  # Đường dẫn đến file Word
    output_dir = "/Users/nguyenvanlam/sources/kidsafe-help/mkdocs/output/"    # Thư mục đầu ra
    create_markdown_from_word(word_file, output_dir)
