---
title: Hướng dẫn tạo user phụ trên Windows để quản lý trẻ em hiệu quả
description: Tạo user phụ trên Windows để hạn chế trẻ em cài phần mềm, bảo vệ dữ liệu và kiểm soát hoạt động máy tính. Hướng dẫn chi tiết, dễ hiểu cho phụ huynh.
keywords:
    - Cách tạo tài khoản phụ trên Windows.
    - Hướng dẫn tạo user con trên máy tính.
    - Quản lý trẻ em trên Windows 10/11.
    - Hạn chế trẻ cài phần mềm trên máy tính.
    - Kiểm soát trẻ em sử dụng máy tính hiệu quả.
    - Tạo tài khoản Standard User Windows.
---

# Hướng dẫn tạo user phụ trên máy tính Windows để quản lý trẻ em

## Giới thiệu

Tạo tài khoản phụ trên Windows là cách giúp phụ huynh quản lý trẻ em sử dụng máy tính. Với tài khoản phụ, trẻ có thể sử dụng máy tính nhưng bị hạn chế cài đặt phần mềm hoặc thay đổi các cài đặt quan trọng. Tài khoản Admin sẽ được giữ bởi phụ huynh để duy trì toàn quyền kiểm soát.

---

## Lợi ích của việc tạo user phụ

-   **Hạn chế cài đặt phần mềm**: Tài khoản phụ không có quyền cài/gỡ phần mềm, giúp bảo vệ hệ thống.
-   **Bảo mật dữ liệu**: Trẻ không thể truy cập hoặc thay đổi các tệp quan trọng.
-   **Dễ dàng quản lý**: Phụ huynh kiểm soát tốt hơn các hoạt động trên máy tính.

---

## Hướng dẫn tạo user phụ trên Windows

### Truy cập quản lý tài khoản

1. Mở **Control Panel** (Bảng điều khiển):
    - Nhấn tổ hợp phím `Windows + S`, gõ **Control Panel**, sau đó nhấn **Enter**.
2. Chọn **User Accounts** (Tài khoản người dùng).
3. Nhấp **Manage another account** (Quản lý tài khoản khác).

---

### Tạo tài khoản người dùng mới

1. Nhấp **Add a new user in PC settings** (Thêm người dùng mới trong cài đặt PC).
2. Trong cửa sổ **Settings**:
    - Chọn **Accounts** (Tài khoản) > **Family & other users** (Gia đình và người dùng khác).
    - Nhấp **Add someone else to this PC** (Thêm người khác vào máy tính này).
3. Chọn **I don't have this person's sign-in information** (Tôi không có thông tin đăng nhập của người này).
4. Nhấp **Add a user without a Microsoft account** (Thêm người dùng mà không cần tài khoản Microsoft).
5. Nhập:
    - **Tên tài khoản** (ví dụ: "User_Con").
    - **Mật khẩu** và xác nhận lại mật khẩu.
6. Nhấn **Next** (Tiếp theo) để hoàn tất.

---

### Tạo tài khoản bằng lệnh netplwiz

1. Nhấn tổ hợp phím `Windows + R` để mở hộp thoại **Run**.
2. Nhập **netplwiz** và nhấn **Enter**.
3. Trong cửa sổ **User Accounts**:
    - Nhấp **Add** (Thêm) để tạo tài khoản mới.
    - Chọn **Sign in without a Microsoft account** (Đăng nhập không cần tài khoản Microsoft), sau đó nhấp **Next**.
    - Nhập **User name** (Tên tài khoản) và **Password** (Mật khẩu). Xác nhận lại mật khẩu.
4. Nhấn **Finish** (Hoàn tất) để tạo tài khoản.
5. Đảm bảo tài khoản được đặt là **Standard User** (Người dùng chuẩn):
    - Chọn tài khoản vừa tạo trong danh sách.
    - Nhấp **Properties** (Thuộc tính) > Tab **Group Membership** (Nhóm thành viên).
    - Chọn **Standard User** và nhấn **OK**.

---

## Thiết lập quyền hạn

1. Quay lại mục **User Accounts** trong **Control Panel** hoặc cửa sổ `netplwiz`.
2. Chọn tài khoản vừa tạo.
3. Nhấp **Change the account type** (Thay đổi loại tài khoản).
4. Đảm bảo tài khoản được đặt là **Standard User** (Người dùng chuẩn), không phải **Administrator**.

---

## Mẹo bảo mật tài khoản Admin

-   **Không chia sẻ mật khẩu Admin**: Chỉ phụ huynh nên biết.
-   **Sử dụng mật khẩu mạnh**: Kết hợp chữ hoa, chữ thường, số và ký tự đặc biệt.
-   **Khóa tài khoản khi không sử dụng**: Nhấn `Windows + L` để khóa nhanh màn hình.

---

Với hướng dẫn này, phụ huynh có thể tạo tài khoản phụ nhanh chóng và tiện lợi bằng công cụ `netplwiz`, đồng thời quản lý hiệu quả hoạt động của trẻ em trên máy tính.
