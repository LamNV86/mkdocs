---
title: Hướng dẫn kiểm soát truy cập web trong KidSafe
description: Hướng dẫn chi tiết cách sử dụng tính năng kiểm soát truy cập web trong KidSafe, bao gồm chặn/mở trang web theo nhóm, chế độ kiểm soát mạng, và tự động cập nhật cơ sở dữ liệu web từ server.
keywords: KidSafe, kiểm soát truy cập web, chặn web, chặn game online, chặn mạng xã hội, quản lý web, hướng dẫn KidSafe
---

# Kiểm soát truy cập web

Tính năng này cho phép:

-   **Chặn truy cập các trang web không mong muốn**: Bao gồm các trang web khiêu dâm, game online, mạng xã hội, và nhiều nhóm khác.
-   **Chặn/mở các trang web theo nhóm**: Các nhóm có sẵn như khiêu dâm, game online, mạng xã hội,… giúp quản lý dễ dàng hơn.
-   **Chặn/mở trang web bất kỳ**: Người dùng có thể tự thêm các URL cụ thể vào danh sách chặn hoặc mở.
-   **Hỗ trợ hai chế độ lọc**:
    -   **Vừa phải**: Cho phép kiểm soát linh hoạt, phù hợp với việc truy cập thông thường.
    -   **Nghiêm ngặt**: Kiểm soát chặt chẽ hơn, ngăn chặn toàn bộ các trang web không phù hợp.
-   **Cơ sở dữ liệu web được cập nhật tự động từ server**: Danh sách các trang web trong nhóm chặn được duy trì và làm mới thường xuyên.

## 2.2.1. Hai chế độ lọc

-   Ở tab "Lọc web", chọn dòng "Chế độ lọc"
-   Ở màn hình "Chế độ lọc web", chọn chế độ soát vừa phải hoặc kiểm soát nghiêm ngặt

  <div class="guide-container guide-grid grid--2-cols">
    <div class="guide-card">
      <div class="guide-title guide-title--5">Vào tab "Lọc web" > dòng "Chế độ lọc"</div>
      <div class="guide-content guide-content--95">
        <img src="../../img/ip43.png" alt="Nhật ký truy cập web">
      </div>
    </div>
    <div></div>
  </div>

 <div class="guide-container guide-grid grid--2-cols">
    <div class="guide-card">
      <div class="guide-title guide-title--5">Kiểm soát vừa phải</div>
      <div class="guide-sub-title guide-sub-title--5">
      Chỉ chặn một số website, tất cả các website khác được mở.
      </div>
      <div class="guide-sub-title guide-sub-title--15">
      - Chọn các nhóm website cần chặn (tích đỏ) => Các website trong các nhóm được chọn sẽ bị chặn truy cập, tất cả các website khác đều vào được.
      </div>
      <div class="guide-content guide-content--75">
        <img src="../../img/ip7.png" alt="Chế độ kiểm soát mạng vừa phải">
      </div>
    </div>
    <div class="guide-card">
      <div class="guide-title guide-title--5">Kiểm soát nghiêm ngặt</div>
      <div class="guide-sub-title guide-sub-title--5">
      Chỉ mở một số website, tất cả các website khác bị chặn.
      </div>
      <div class="guide-sub-title guide-sub-title--15">
      - Chọn các nhóm website được mở (tích xanh) => Các website trong các nhóm được chọn sẽ được mở truy cập, tất cả các website khác sẽ bị chặn.
      </div>
      <div class="guide-content guide-content--75">
        <img src="../../img/ip8.png" alt="Chế độ kiểm soát mạng nghiêm ngặt">
      </div>
    </div>

  </div>

## 2.2.2. Chặn/mở truy cập website theo nhóm

-   Ở tab Lọc web > Lọc nhóm: Mỗi nhóm website hiển thị thành 1 dòng

  <div class="guide-container guide-grid grid--2-cols">
    <div class="guide-card">
      <div class="guide-title guide-title--15">Ở chế độ kiểm soát vừa phải: tích đỏ là chặn, không tích là mở</div>
      <div class="guide-content guide-content--85">  
        <img src="../../img/wm-normal.png" alt="Chế độ kiểm soát mạng vừa phải">
      </div>
    </div>
    <div class="guide-card">
      <div class="guide-title guide-title--15">Ở chế đố kiểm soát nghiêm ngặt: tích xanh là mở, không tích là chặn</div>
      <div class="guide-content guide-content--85">  
        <img src="../../img/wm-strict.png" alt="Chế độ kiểm soát mạng nghiêm ngặt">
      </div>
    </div>
  </div>

-   Ở tab Lọc web > Chi tiết: xem cụ thể từng trang web

 <div class="guide-container guide-grid grid--2-cols">
    <div class="guide-card">
      <div class="guide-title guide-title--10">Khi nhóm Game online bị chặn (tích đỏ) thì tất cả game online trong nhóm bị chặn</div>
      <div class="guide-sub-title guide-sub-title--15">
        <img src="../../img/wm-block-group.png" alt="">
      </div>
      <div class="guide-content guide-content--75">  
        <img src="../../img/ip9.png" alt="">
      </div>
    </div>
    <div class="guide-card">
      <div class="guide-title guide-title--10">Khi nhóm Game online được mở (không tích) thì tất cả game online trong nhóm được mở</div>
      <div class="guide-sub-title guide-sub-title--15">
        <img src="../../img/wm-allow-group.png" alt="">
      </div>
      <div class="guide-content guide-content--75">  
        <img src="../../img/ip10.png" alt="">
      </div>
    </div>
  </div>

## 2.2.3. Chặn/mở truy cập website đơn lẻ có sẵn

-   Vào tab “Lọc web” > tab “Chi tiết” > nhấn vào ô Tìm kiếm > nhập tên website để tìm
-   Gạt công tắc sang màu xanh để mở chặn, gạt sang màu đỏ đề chặn

  <div class="guide-container guide-grid grid--3-cols">
    <div class="guide-card">
      <div class="guide-title guide-title--15 guide-title--bullet">Tab “Lọc web” > tab “Chi tiết” > ô Tìm kiếm > nhập tên website để tìm</div>
      <div class="guide-content guide-content--85">  
        <img src="../../img/ip11.png" alt="Tab lọc chi tiết">
      </div>
    </div>
    <div class="guide-card">
      <div class="guide-title guide-title--15 guide-title--bullet">Gạt công tắc sang màu xanh để mở chặn</div>
      <div class="guide-content guide-content--85">  
        <img src="../../img/ip12.png" alt="Mở 1 trang web">
      </div>
    </div>
    <div class="guide-card">
      <div class="guide-title guide-title--15 guide-title--bullet">Gạt công tắc sang màu đỏ đề chặn</div>
      <div class="guide-content guide-content--85">  
        <img src="../../img/ip13.png" alt="Chặn 1 trang web">
      </div>
    </div>    
  </div>

## 2.2.4. Chặn/mở truy cập website bất kỳ

 <div class="guide-container guide-grid grid--2-cols">
    <div class="guide-card">
      <div class="guide-title guide-title--10">Tab “Lọc web” > tab “Lọc nhanh” > tab "Chặn"</div>
      <div class="guide-sub-title guide-sub-title--15">
      Chọn sẵn các trang như youtube, facebook, zalo, tiktok hoặc nhập trang bất kỳ để chặn. <br>
          => Các trang ở đây sẽ luôn luôn bị chặn.
      </div>
      <div class="guide-content guide-content--75">  
        <img src="../../img/ip15.png" alt="Tab lọc chi tiết">
      </div>
    </div>
    <div class="guide-card">
      <div class="guide-title guide-title--10">Tab “Lọc web” > tab “Lọc nhanh” > tab "Mở"</div>
      <div class="guide-sub-title guide-sub-title--15">
        Chọn sẵn các trang như youtube, facebook, zalo, tiktok hoặc nhập trang bất kỳ để mở. <br>
        => Các trang ở đây sẽ luôn luôn được mở.
      </div>
      <div class="guide-content guide-content--75">  
        <img src="../../img/ip16.png" alt="Mở trang web bất kỳ">
      </div>
    </div>
  </div>

---

## Lợi ích

-   Đảm bảo an toàn khi truy cập internet cho trẻ bằng cách chặn các trang web không phù hợp.
-   Dễ dàng quản lý các nhóm trang web với danh sách được cập nhật tự động.
-   Linh hoạt trong việc chặn hoặc mở các trang web theo nhu cầu thực tế.
-   Hai chế độ kiểm soát mạng giúp phụ huynh điều chỉnh phù hợp với từng tình huống:

    -   Có thể chọn kiểm soát vừa phải, sau đó theo dõi con vào trang web nào? nếu không muốn con vào trang đó thì chặn lại (xem thêm [Lịch sử truy cập web](/usage-guide/usage-history/#xem-lich-su-truy-cap-cac-trang-web))
    -   Hoặc chọn chế độ kiểm soát nghiêm ngặt, nếu con vào trang nào đó bị chặn thì có thể mở ra (xem thêm [2.2.4](/usage-guide/web-control/#224-chanmo-truy-cap-website-bat-ky))
