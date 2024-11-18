import os
from docx import Document
from docx.shared import Inches

# Định nghĩa tên file Markdown tương ứng với các mục lục
md_file_mapping = {
    'Tải ứng dụng và cài đặt trên máy tính': 'install-guide/install-on-computer.md',
    'Kích hoạt licence & lấy mã kích hoạt': 'install-guide/activate-license.md',
    'Cài đặt phần mềm KidSafe Admin trên điện thoại': 'install-guide/install-on-phone.md',
    'Liên kết máy tính với điện thoại': 'install-guide/link-computer-to-phone.md',
    'Bật/tắt các tính năng': 'usage-guide/quick-control/toggle-features.md',
    'Khoá/mở khoá máy tính': 'usage-guide/quick-control/lock-unlock.md',
    'Hai chế độ kiểm soát mạng': 'usage-guide/web-control/modes.md',
    'Chặn/mở truy cập website theo nhóm': 'usage-guide/web-control/block-unblock-groups.md',
    'Chặn/mở chặn truy cập website đơn lẻ có sẵn': 'usage-guide/web-control/block-unblock-individual.md',
    'Chặn/mở nhanh 1 trang web bất kỳ': 'usage-guide/web-control/quick-block-unblock.md',
    'Xem ảnh chụp màn hình': 'usage-guide/screenshot/view-screenshots.md',
    'Thay đổi cấu hình chụp ảnh': 'usage-guide/screenshot/change-settings.md',
    'Lịch sử truy cập web': 'usage-guide/web-history.md',
    'Lịch sử chạy ứng dụng trên máy': 'usage-guide/app-history.md',
    'Chặn/mở chặn một game': 'usage-guide/game-blocking/block-unblock.md',
    'Thêm mới 1 game vào danh sách chặn': 'usage-guide/game-blocking/add-to-blocklist.md',
    'Lập lịch khoá theo khung giờ': 'usage-guide/schedule/lock-schedule.md',
    'Màn hình khoá máy tính': 'usage-guide/schedule/lock-screen.md',
    'Lập lịch chặn game/ứng dụng': 'usage-guide/schedule/block-schedule.md',
    'Cập nhật CSDL web': 'usage-guide/database-update.md',
    'Cài đặt chung': 'usage-guide/general-settings.md'
}

# Hàm để tạo file Markdown từ tiêu đề và nội dung
def create_md_file(filename, content):
    # Tạo thư mục nếu chưa tồn tại
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Đã tạo file: {filename}")

# Hàm để lưu ảnh từ tài liệu Word
def save_image(image, output_dir, image_index):
    image_filename = os.path.join(output_dir, f"image_{image_index}.png")
    with open(image_filename, "wb") as img_file:
        img_file.write(image._blob)
    return image_filename

# Hàm chuyển đổi file Word thành các file Markdown
def convert_word_to_md(docx_path, output_dir):
    # Mở file Word
    try:
        doc = Document(docx_path)
    except Exception as e:
        print(f"Không thể mở file Word: {e}")
        return
    
    # Tạo thư mục output nếu chưa tồn tại
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    content = ""
    previous_heading = None
    current_level = 0
    image_index = 1

    # Duyệt qua từng đoạn văn trong file Word
    for para in doc.paragraphs:
        text = para.text.strip()
        if text == "" and not para.runs:
            continue
        
        # Kiểm tra cấp độ tiêu đề dựa trên định dạng
        if para.style.name.startswith('Heading 1'):
            level = 1
        elif para.style.name.startswith('Heading 2'):
            level = 2
        elif para.style.name.startswith('Heading 3'):
            level = 3
        else:
            level = 0

        if level > 0:
            # Lưu nội dung của phần trước đó nếu có
            if previous_heading and content:
                filename = md_file_mapping.get(previous_heading, None)
                if filename:
                    filename = os.path.join(output_dir, filename)
                    create_md_file(filename, content)
                else:
                    print(f"Không tìm thấy tên file cho tiêu đề: {previous_heading}")
                content = ""
            
            # Cập nhật tên mục hiện tại
            previous_heading = text
            current_level = level
            if level == 1:
                content = f"# {text}\n\n"
            elif level == 2:
                content = f"## {text}\n\n"
            elif level == 3:
                content = f"### {text}\n\n"
            print(f"Phát hiện tiêu đề cấp {level}: {text}")
        else:
            # Thêm nội dung vào phần hiện tại
            content += f"{text}\n\n"

        # Lưu các hình ảnh trong đoạn văn
        for run in para.runs:
            if run.element.tag.endswith('}drawing') or run.element.tag.endswith('}pict'):
                image_filename = save_image(run._element, output_dir, image_index)
                content += f"![Image {image_index}]({image_filename})\n\n"
                image_index += 1

    # Lưu phần cuối cùng
    if previous_heading and content:
        filename = md_file_mapping.get(previous_heading, None)
        if filename:
            filename = os.path.join(output_dir, filename)
            create_md_file(filename, content)
        else:
            print(f"Không tìm thấy tên file cho tiêu đề: {previous_heading}")

# Đường dẫn tới file Word và thư mục đầu ra
docx_path = "/Users/nguyenvanlam/sources/document/System/KidSafe/Guide/HD_cai_dat_va_su_dung_KidSafe_v2.0.docx"  # Đường dẫn đến file Word
output_dir = "/Users/nguyenvanlam/sources/kidsafe-help/mkdocs/output/"

# Chuyển đổi file Word thành các file Markdown
convert_word_to_md(docx_path, output_dir)

print(f"Chuyển đổi hoàn tất! Các file Markdown được lưu trong thư mục '{output_dir}'")
