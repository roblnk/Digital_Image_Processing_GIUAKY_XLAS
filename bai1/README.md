3.1 Color Transforms

Cách chạy: cd vào thư mục bai1 và gõ lần lượt các câu lệnh sau vào terminal:

    python bai1_color_balance.py


- Giải thích: 
Xác định tỷ lệ cân bằng màu mặc định là 1,0 cho mỗi kênh màu đỏ, xanh làm và xanh lục. Sau đó, xác định GUI bằng thư viện Tkinter cho phép người dùng điều chỉnh tỷ lệ cân bằng màu bằng thanh trượt. Thanh trượt cập nhật tỷ lệ cân bằng màu và áp dụng biến đổi bằng cách sử dụng hàm apply_color_balance().

Hàm apply_color_balance() chia hình ảnh thành các kênh màu của nó, áp dụng tỷ lệ cân bằng màu cho từng kênh và hợp nhất các kênh lại thành một hình ảnh. Hàm np.clip() được sử dụng để đảm bảo rằng các giá trị màu nằm trong phạm vi hợp lệ từ 0-255.

- Câu hỏi:
1. Bạn có nhận được các kết quả khác nhau nếu loại bỏ phép biến đổi gamma trước hoặc sau khi thực hiện phép nhân không? Tại sao hay tại sao không?
+ Trả lời: Có, ta có thể nhận được các kết quả khác nếu chúng ta loại bỏ phép biến đổi gamma trước hoặc sau khi thực hiện phép nhân. Biến đổi gamma là một phép toán phi tuyến tính, do đó, nó ảnh hưởng đến sự phân bố màu sắc khác với phép toán nhân tuyến tính. Ví dụ: nếu trước tiên ta áp dụng phép biến đổi gamma để tăng độ tương phản của hình ảnh, sau đó thực hiện phép nhân cân bằng màu, thì các thay đổi về cân bằng màu sẽ dễ nhận thấy hơn ở các tông màu trung tính và bóng tối, trong khi các vùng sáng có thể tương đối không thay đổi. Mặt khác, nếu ta thực hiện phép nhân trước và sau đó áp dụng phép biến đổi gamma, các thay đổi về cân bằng màu sẽ được phân bổ đồng đều hơn trên phạm vi tông màu của hình ảnh.

2. Chụp cùng một bức ảnh bằng máy ảnh kỹ thuật số của bạn bằng cách sử dụng các cài đặt cân bằng màu khác nhau (hầu hết các máy ảnh kiểm soát cân bằng màu từ một trong các menu). Bạn có thể khôi phục tỷ lệ cân bằng màu giữa các cài đặt khác nhau không? Bạn có thể cần đặt máy ảnh của mình lên giá ba chân và căn chỉnh hình ảnh theo cách thủ công hoặc tự động để thực hiện công việc này.
+ Trả lời: Có, có thể khôi phục tỷ lệ cân bằng màu giữa các cài đặt khác nhau bằng cách so sánh biểu đồ màu của hình ảnh. Nếu ta chụp nhiều ảnh của cùng một cảnh với các cài đặt cân bằng màu khác nhau, biểu đồ màu của mỗi ảnh sẽ có hình dạng và vị trí đỉnh khác nhau. Bằng cách phân tích sự khác biệt giữa các biểu đồ, ta có thể ước tính tỷ lệ cân bằng màu được sử dụng cho mỗi hình ảnh.

3. Bạn có thể nghĩ ra bất kỳ lý do nào khiến bạn có thể muốn thực hiện một sự thay đổi màu sắc trên hình ảnh không?
+ Trả lời: Vâng, có một số lý do tại sao bạn có thể muốn thực hiện một sự thay đổi màu sắc trên hình ảnh. Một lý do là để sửa các hiện tượng đổ màu do điều kiện ánh sáng hoặc cài đặt máy ảnh gây ra. Ví dụ: nếu ảnh được chụp dưới ánh sáng trong nhà có vẻ quá ấm (cam/vàng), bạn có thể áp dụng hiệu ứng xoắn màu để chuyển màu về phía cuối quang phổ lạnh hơn (lam/lục). Một lý do khác là để tạo hiệu ứng nghệ thuật hoặc nâng cao các tính năng nhất định của hình ảnh. Ví dụ: bạn có thể áp dụng một vòng xoắn màu để nhấn mạnh các tông màu xanh lam trong ảnh phong cảnh để làm cho bầu trời có vẻ rực rỡ hơn.

- input: input_image_cat.jpg
- output: giao diện Tkinter và ảnh input

