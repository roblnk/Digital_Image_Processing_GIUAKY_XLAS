3.15 Distance transform

Cách chạy: cd vào thư mục bai8 và gõ lần lượt các câu lệnh sau vào terminal:

    python bai8_distance_transform.py


Giải thích: 
+ Hình ảnh đầu vào được tải dưới dạng hình ảnh thang độ xám trong đó các pixel nền trước được biểu thị bằng 0 và pixel nền là 255 giây.

+ Hình ảnh được đảo ngược bằng cách sử dụng hàm cv2.bitwise_not để tạo các pixel nền trước là 255 và các pixel nền là 0. Bước này là cần thiết vì biến đổi khoảng cách của OpenCV giả định các pixel nền trước là 0 và các pixel nền là các giá trị khác không.

+ Biến đổi khoảng cách khối thành phố được tính toán bằng cách sử dụng hàm cv2. distanceTransform với tham số cv2.DIST_L1, chỉ định số liệu khoảng cách là khoảng cách khối thành phố.

+ Tương tự, phép biến đổi khoảng cách Euclide được tính toán bằng cách sử dụng hàm cv2. distanceTransform với tham số cv2.DIST_L2, chỉ định số liệu khoảng cách là khoảng cách Euclide.

+ Các biến đổi khoảng cách sau đó được chuẩn hóa bằng cách sử dụng hàm cv2.normalize để đảm bảo các giá trị của chúng nằm trong phạm vi từ 0 đến 255 cho mục đích trực quan hóa.

+ Cuối cùng, các hình ảnh được biến đổi khoảng cách được hiển thị bằng hàm cv2.imshow.

+ Cách tiếp cận này thúc đẩy các thuật toán biến đổi khoảng cách được tối ưu hóa được triển khai trong OpenCV, cung cấp khả năng tính toán chính xác và hiệu quả hơn đối với các biến đổi khoảng cách Euclide và khối thành phố.
- input: hand.jpg
- output: các bức ảnh với kết quả biến đổi khoảng cách Euclide và city block
