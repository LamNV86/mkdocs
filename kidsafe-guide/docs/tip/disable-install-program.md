---
title: "Hướng dẫn disable tài khoản phụ cài đặt phần mềm trên Windows"
description: "Hướng dẫn chi tiết cách vô hiệu hóa tài khoản phụ cài đặt phần mềm trên Windows. Bảo vệ hệ thống và quản lý trẻ em hiệu quả với các bước đơn giản."
keywords: "disable tài khoản phụ, hạn chế cài đặt phần mềm, bảo mật Windows, quản lý trẻ em, chặn cài đặt phần mềm Windows"
---

# Hướng dẫn disable tài khoản phụ cài đặt phần mềm trên Windows

## Giới thiệu

Việc vô hiệu hóa quyền cài đặt phần mềm của tài khoản phụ giúp bảo vệ hệ thống khỏi những ứng dụng không mong muốn, đồng thời đảm bảo trẻ em không thể tự ý cài đặt phần mềm trên máy tính.

---

## Cách vô hiệu hóa tài khoản phụ cài đặt phần mềm

### 1. Đặt tài khoản phụ là Standard User

1. Đảm bảo tài khoản phụ **không phải** tài khoản Admin:
    - Mở **Control Panel** > **User Accounts**.
    - Nhấp vào tài khoản phụ, chọn **Change the account type**.
    - Chọn **Standard User** và nhấn **OK**.

---

### 2. Sử dụng Group Policy Editor (Chỉ áp dụng cho Windows Pro/Enterprise)

1. Nhấn tổ hợp phím `Windows + R`, nhập **gpedit.msc**, nhấn **Enter**.
2. Truy cập đường dẫn:
   Computer Configuration > Administrative Templates > Windows Components > Windows Installer

3. Tìm và mở mục **Prohibit User Installs** (Ngăn người dùng cài đặt).
4. Chọn **Enabled** (Bật), sau đó nhấn **OK**.

---

### 3. Hạn chế quyền truy cập file cài đặt

1. Tìm đến thư mục chứa các tệp cài đặt phần mềm, ví dụ:

-   **C:\Windows\System32\msiexec.exe** (Trình cài đặt MSI).
-   Các tệp cài đặt `.exe` thường được tải xuống từ **Downloads**.

2. Nhấp chuột phải vào tệp hoặc thư mục, chọn **Properties** (Thuộc tính).
3. Chuyển sang tab **Security** (Bảo mật):

-   Nhấp **Edit** (Chỉnh sửa).
-   Chọn tài khoản phụ, sau đó tích chọn **Deny** (Từ chối) với quyền **Full control** (Toàn quyền).

---

### 4. Tắt quyền cài đặt từ Microsoft Store

1. Mở **Settings** (Cài đặt) > **Accounts** > **Family & other users**.
2. Nhấp vào tài khoản phụ > **Change account type**.
3. Đặt tài khoản phụ là **Standard User**.
4. Vào mục **Settings** > **Apps** > **Apps & features**:

-   Trong phần **Installing apps**, chọn **Allow apps from the Store only** (Chỉ cho phép ứng dụng từ Microsoft Store).

---

### 5. Sử dụng Registry Editor (Dành cho người dùng nâng cao)

1. Nhấn tổ hợp phím `Windows + R`, nhập **regedit**, nhấn **Enter**.
2. Truy cập đường dẫn:
   HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\Installer

3. Tạo một giá trị DWORD (32-bit) mới:

-   Tên: **DisableMSI**
-   Giá trị: `2` (Ngăn tất cả người dùng cài đặt phần mềm).

4. Nhấn **OK**, sau đó khởi động lại máy tính.

---

## Mẹo bảo mật bổ sung

-   **Giám sát hoạt động tài khoản phụ**: Kiểm tra thường xuyên các ứng dụng đã cài đặt.
-   **Không chia sẻ mật khẩu Admin**: Chỉ phụ huynh nắm giữ tài khoản Admin.
-   **Khóa quyền truy cập tải xuống**: Kiểm soát quyền vào thư mục tải xuống hoặc chặn các trang web tải phần mềm.

---

Bằng cách thực hiện các bước trên, bạn có thể dễ dàng kiểm soát quyền cài đặt phần mềm của tài khoản phụ, giúp bảo vệ hệ thống và quản lý hoạt động trên máy tính một cách hiệu quả.
