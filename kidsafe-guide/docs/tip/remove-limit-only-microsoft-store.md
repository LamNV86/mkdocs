
# Hướng dẫn bỏ giới hạn chỉ cài đặt ứng dụng từ Microsoft Store

## 1. Thông qua Settings
1. Mở **Settings** (Nhấn `Windows + I`).
2. Điều hướng đến **Apps > Apps & Features**.
3. Tại mục **Choose where to get apps**, chọn **Anywhere** (Thay vì "The Microsoft Store only (Recommended)").

---

## 2. Thông qua Local Group Policy Editor (Windows Pro/Enterprise)
1. Nhấn `Windows + R`, nhập `gpedit.msc`, và nhấn **Enter**.
2. Điều hướng đến:
   ```
   Computer Configuration > Administrative Templates > Windows Components > App Package Deployment
   ```
3. Tìm tùy chọn **Allow all trusted apps to install**:
   - Đặt thành **Enabled** hoặc **Not Configured**.
4. Tiếp tục điều hướng đến:
   ```
   Computer Configuration > Administrative Templates > System
   ```
5. Tìm **Only display the Store apps on Windows 10/11**:
   - Đặt thành **Disabled**.

---

## 3. Thông qua Registry Editor (Windows Home)
1. Nhấn `Windows + R`, nhập `regedit`, và nhấn **Enter**.
2. Điều hướng đến:
   ```
   HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer
   ```
3. Kiểm tra và chỉnh sửa:
   - Nếu có khóa `AicEnabled`, xóa nó hoặc đặt giá trị thành `0`.
4. Nếu không có khóa này, không cần chỉnh sửa gì thêm.

---

## 4. Khởi động lại máy
- Sau khi thực hiện các thay đổi, khởi động lại máy để áp dụng cài đặt mới.

---

> **Lưu ý**: Các thay đổi này sẽ cho phép bạn cài đặt ứng dụng từ bất kỳ nguồn nào, không chỉ giới hạn Microsoft Store.
