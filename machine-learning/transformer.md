# Transformer

## Transformer Architecture

Kiến trúc Transformer là một mô hình học sâu phổ biến được giới thiệu trong bài báo "Attention is All You Need" của Vaswani và đồng nghiệp (2017). Nó đã cách mạng hóa nhiều nhiệm vụ xử lý ngôn ngữ tự nhiên (NLP) và trở thành cơ sở cho các mô hình tiên tiến như BERT và GPT.

Kiến trúc Transformer dựa trên khái niệm self-attention, cho phép mô hình tập trung vào các phần khác nhau của chuỗi đầu vào khi xử lý từng phần tử. Dưới đây là một cái nhìn tổng quan về kiến trúc Transformer:

![Kiến trúc Transformer](https://d2l.ai/_images/transformer.svg)

1. Nhúng Đầu Vào (Input Embeddings):
   - Chuỗi đầu vào được nhúng thành các biểu diễn liên tục được gọi là nhúng đầu vào.
   - Mỗi từ hoặc thành phần trong chuỗi đầu vào được biểu diễn bằng một vector mật độ.

2. Mã Hóa Vị Trí (Positional Encoding):
   - Mã hóa vị trí được thêm vào nhúng đầu vào để cung cấp thông tin về thứ tự hoặc vị trí của các từ trong chuỗi.
   - Điều này cho phép mô hình bắt chước thông tin tuần tự, vì kiến trúc Transformer không có kết nối lặp lại.

3. Bộ Mã Hóa (Encoder):
   - Transformer bao gồm một cấu trúc mã hóa-giải mã (encoder-decoder), nhưng để đơn giản, chúng ta tập trung vào bộ mã hóa.
   - Bộ mã hóa bao gồm nhiều lớp giống nhau, mỗi lớp bao gồm hai lớp con:
     a. Multi-head Self-Attention:
        - Self-attention cho phép mô hình đánh trọng số sự quan trọng của các từ khác nhau trong chuỗi đầu vào khi xử lý một từ cụ thể.
        - Nó tính toán tổng `trọng số` của các nhúng từ tất cả các từ, trong đó `trọng số` được xác định bởi `sự tương đồng giữa` các từ.
     b. Feed-Forward Neural Network:
        - A simple feed-forward neural network được áp dụng cho từng vị trí trong chuỗi độc lập.
        - Nó giúp bắt chước mối quan hệ phi tuyến giữa các từ trong chuỗi.

4. Bộ Giải Mã (Decoder):
   - Bộ giải mã tương tự như bộ mã hóa nhưng có cơ chế attention bổ sung.
   - Nó tạo ra chuỗi đầu ra bằng cách chú ý đến các biểu diễn đầu ra của bộ mã hóa và các từ đã được tạo ra trước đó.

5. Cơ Chế Che (Masking):
   - Trong quá trình huấn luyện, cơ chế che được sử dụng để ngăn mô hình chú ý đến các vị trí trong tương lai.
   - Điều này đảm bảo rằng mỗi vị trí chỉ có thể chú ý đến các vị trí trước đó trong chuỗi đầu vào.

6. Tạo Ra Đầu Ra:
   - Lớp cuối cùng của bộ giải mã tạo ra xác suất đầu ra cho mỗi vị trí trong chuỗi đầu ra.
   - Các xác suất này thường được tính bằng cách sử dụng hàm kích hoạt softmax.

Kiến trúc Transformer có một số lợi thế, như khả năng song song hóa, khả năng bắt chước các phụ thuộc xa, và khả năng tổng quát tốt hơn nhờ self-attention. Nó đã đạt được kết quả tiên tiến trên nhiều nhiệm vụ NLP, bao gồm dịch máy, tóm tắt văn bản và hiểu ngôn ngữ.


## Self Attention

### What is Self Attention?

Self-attention, còn được gọi là intra-attention hay scaled [dot-product](https://www.mathsisfun.com/algebra/vectors-dot-product.html) attention (tích vô hướng giữa 2 vector), là một cơ chế tính toán trọng số chú ý cho các phần tử trong cùng một chuỗi đầu vào. Nó cho phép mô hình đánh giá mức độ quan trọng của mỗi phần tử trong chuỗi dựa trên mức liên quan của nó đối với các phần tử khác. 

### Example

Trong self-attention, mỗi từ trong chuỗi đầu vào được biểu diễn bằng một vector, thông thường được gọi là nhúng hay vector nhúng (embedding vector). Giả sử nhúng từ cho chuỗi đầu vào như sau:

Ví dụ câu như sau: "Con mèo ngồi trên chiếc thảm."

Để áp dụng self-attention, chúng ta trước tiên biểu diễn mỗi từ trong câu thành một `vector nhúng`. Hãy giả sử chúng ta có các vector nhúng từ sau đây:

Nhúng từ:

    - "Con": [0.2, 0.5, -0.3]
    - "mèo": [-0.1, 0.7, 0.2]
    - "ngồi": [0.4, -0.2, 0.6]
    - "trên": [-0.5, 0.3, -0.1]
    - "chiếc": [0.2, 0.5, -0.3]
    - "thảm": [0.3, 0.1, 0.8]
    - ".": [0.0, 0.0, 0.0]

Bây giờ, chúng ta tính toán `trọng số self-attention` cho mỗi từ trong câu. Trong self-attention, mỗi từ được so sánh với tất cả các từ khác để xác định độ quan trọng hoặc liên quan của nó. Quá trình so sánh được thực hiện bằng cách tính tích vô hướng giữa nhúng từ, sau đó áp dụng phép softmax để thu được trọng số chú ý.

Ví dụ, đối với từ "Con," tích vô hướng được tính toán với nhúng từ của tất cả các từ khác:

Trọng số Chú ý cho "Con":

    - "Con" so sánh với "Con": 0.3
    - "Con" so sánh với "mèo": 0.1
    - "Con" so sánh với "ngồi": 0.2
    - "Con" so sánh với "trên": 0.05
    - "Con" so sánh với "chiếc": 0.35
    - "Con" so sánh với "thảm": 0.0
    - "Con" so sánh với ".": 0.0

Các trọng số chú ý phản ánh sự quan trọng của mỗi từ đối với "Con" dựa trên sự tương đồng ngữ nghĩa hoặc liên quan ngữ cảnh của chúng. Phép *softmax đảm bảo rằng các trọng số tổng cộng bằng 1*.

Chúng ta lặp lại quá trình này cho mỗi từ trong câu để thu được trọng số self-attention cho toàn bộ câu. Những trọng số chú ý này sau đó có thể được sử dụng để tổng hợp thông tin từ các từ khác nhau và bắt chước các mối quan hệ quan trọng trong câu để tiếp tục xử lý trong mô hình.


## Multi-Head Attention

### Multi-Head Attention là gì?

Multi-Head Attention là một phần mở rộng của self-attention cho phép mô hình tập trung vào các khía cạnh khác nhau của chuỗi đầu vào cùng một lúc. Đó là việc áp dụng self-attention nhiều lần song song, mỗi attention head tập trung vào một biểu diễn khác nhau của đầu vào. Bằng cách sử dụng nhiều attention head, mô hình có thể nắm bắt các thông tin khác nhau và học các mẫu đa dạng, nâng cao khả năng hiểu và xử lý các chuỗi phức tạp một cách hiệu quả.

### Ví dụ

   1. Xem xét một câu tiếng Anh: "I love cats." -> Và chúng ta muốn dịch nó sang tiếng Pháp: "J'adore les chats."

   1. Giả sử cả hai câu tiếng Anh và tiếng Pháp đã được nhúng thành các vector như sau:

      Nhúng từ tiếng Anh:

         - "I": [0.1, 0.2, 0.3]
         - "love": [0.4, 0.5, 0.6]
         - "cats": [0.7, 0.8, 0.9]

      Nhúng từ tiếng Pháp:

         - "J'adore": [0.9, 0.8, 0.7]
         - "les": [0.6, 0.5, 0.4]
         - "chats": [0.3, 0.2, 0.1]

   1. Tính toán trọng số

      - Giả sử chúng ta đang sử dụng cơ chế multi-head attention với `2 attention head`. Mỗi head sẽ tập trung vào chuỗi đầu vào tiếng Anh (nguồn) và chuỗi đầu vào tiếng Pháp (đích) riêng biệt.

      - Với mỗi attention head, chúng ta sẽ tính toán `trọng số attention` cho cả chuỗi đầu vào tiếng Anh và tiếng Pháp. Các trọng số attention xác định mức độ quan trọng của mỗi từ trong chuỗi nguồn liên quan đến các từ trong chuỗi đích.

      - Ví dụ, 

      Với attention head đầu tiên, chúng ta tính toán trọng số attention cho chuỗi đầu vào tiếng Anh:

      `Attention_scores_source_head1 = softmax(dot_product(english_source_embeddings, [french_target_embedding1, french_target_embedding2, french_target_embedding3]))`

      Tương tự, chúng ta tính toán trọng số attention cho chuỗi đích tiếng Pháp:

      `Attention_scores_target_head1 = softmax(dot_product(french_target_embeddings, [english_source_embedding1, english_source_embedding2, english_source_embedding3]))`

      Lặp lại các bước trên cho attention head tiếp theo, kết quả sẽ được các `attention score` cho cả chuỗi nguồn và chuỗi đích.

   1. Sau khi có các trọng số attention, chúng ta áp dụng chúng vào nhúng tương ứng để có tổng có trọng số cho mỗi chuỗi.

      Ví dụ, đối với chuỗi nguồn tiếng Anh và attention head đầu tiên:

      `Weighted_sum_source_head1 = attention_score1 * english_source_embedding1 + attention_score2 * english_source_embedding2 + attention_score3 * english_source_embedding3`

      Tương tự, đối với chuỗi đích tiếng Pháp và attention head đầu tiên:

      `Weighted_sum_target_head1 = attention_score1 * french_target_embedding1 + attention_score2 * french_target_embedding2 + attention_score3 * french_target_embedding3`

   1. Chúng ta lặp lại các bước trên cho attention head thứ hai.

      Cuối cùng, chúng ta nối các đầu ra từ mỗi attention head và thông qua một phép biến đổi tuyến tính để có đầu ra multi-head attention cuối cùng.

      Như vậy, cơ chế multi-head attention cho phép mô hình nắm bắt các thông tin và mối quan hệ khác nhau giữa chuỗi nguồn và chuỗi đích, tăng khả năng dịch giữa các ngôn ngữ một cách chính xác.


### Code illustration

```python
import torch
import torch.nn as nn

class MultiHeadAttention(nn.Module):
    def __init__(self, embed_dim, num_heads):
        super(MultiHeadAttention, self).__init__()
        
        self.embed_dim = embed_dim
        self.num_heads = num_heads
        self.head_dim = embed_dim // num_heads
        
        self.query_projection = nn.Linear(embed_dim, embed_dim)
        self.key_projection = nn.Linear(embed_dim, embed_dim)
        self.value_projection = nn.Linear(embed_dim, embed_dim)
        self.output_projection = nn.Linear(embed_dim, embed_dim)
        
    def forward(self, query, key, value):
        batch_size = query.size(0)
        
        # Apply linear projections for query, key, and value
        query = self.query_projection(query)
        key = self.key_projection(key)
        value = self.value_projection(value)
        
        # Reshape query, key, and value to split heads
        query = query.view(batch_size, -1, self.num_heads, self.head_dim).transpose(1, 2)
        key = key.view(batch_size, -1, self.num_heads, self.head_dim).transpose(1, 2)
        value = value.view(batch_size, -1, self.num_heads, self.head_dim).transpose(1, 2)
        
        # Compute attention scores
        scores = torch.matmul(query, key.transpose(-2, -1))
        scores = scores / torch.sqrt(torch.tensor(self.head_dim, dtype=torch.float32))
        attention_weights = torch.softmax(scores, dim=-1)
        
        # Apply attention weights to value
        attended_values = torch.matmul(attention_weights, value)
        
        # Reshape and concatenate attended values
        attended_values = attended_values.transpose(1, 2).contiguous().view(batch_size, -1, self.embed_dim)
        
        # Apply linear projection for output
        output = self.output_projection(attended_values)
        
        return output

```

## Positional Encoding

### What is Positional Encoding?
- Phép mã hóa vị trí (Positional Encoding) là một kỹ thuật được sử dụng trong các mô hình dựa trên chuỗi, đặc biệt là trong kiến trúc Transformer, để đưa thông tin về vị trí tương đối của các yếu tố trong chuỗi đầu vào. Nó giải quyết vấn đề rằng tự chú ý (self-attention) và các cơ chế chú ý khác trong các mô hình này không ngầm định mã hóa thông tin về vị trí.

- Trong các nhiệm vụ xử lý ngôn ngữ tự nhiên, thứ tự của các từ trong một câu mang ý nghĩa và ngữ cảnh quan trọng. Tuy nhiên, mô hình Transformer xử lý chuỗi đầu vào theo cách song song, không rõ ràng ghi nhận thứ tự tuần tự. Phép mã hóa vị trí giúp mô hình phân biệt giữa các yếu tố ở các vị trí khác nhau trong chuỗi.

- Mã hóa vị trí được thêm vào nhúng đầu vào của chuỗi trước khi đưa chúng vào mô hình Transformer. Thông thường, điều này được thực hiện bằng cách kết hợp các hàm sin-cos với các nhúng đầu vào. Mỗi chiều của mã hóa vị trí đại diện cho một vị trí cụ thể trong chuỗi.

- Sự lựa chọn các hàm sin-cos cho phép mô hình dễ dàng mở rộng cho các độ dài chuỗi dài hơn so với những gì mô hình đã được huấn luyện. Tần số của các hàm sin-cos tuân theo một cấp số học, cho phép mô hình học để chú ý đến các vị trí khác nhau với các tỷ lệ khác nhau.

- Bằng cách thêm mã hóa vị trí vào nhúng đầu vào, mô hình Transformer có thể hiệu quả nắm bắt thứ tự và vị trí tương đối của các yếu tố trong chuỗi. Điều này giúp mô hình hiểu các phụ thuộc và mối quan hệ giữa các vị trí khác nhau và cho phép thực hiện các nhiệm vụ yêu cầu xử lý thông tin tuần tự, chẳng hạn như dịch máy hoặc hiểu ngôn ngữ.

### Ví dụ

Giả sử chúng ta có một chuỗi đầu vào gồm ba từ: ["Tôi", "yêu", "mèo"].

Mỗi từ sẽ được biểu diễn bằng một vector nhúng từ, nắm bắt ý nghĩa ngữ nghĩa của nó. Hãy giả định các vector nhúng từ như sau:

- "Tôi": [0.2, 0.3, -0.1]
- "yêu": [-0.5, 0.7, 0.2]
- "mèo": [0.7, 0.8, 0.9]

Để tích hợp thông tin về vị trí, chúng ta sử dụng mã hóa vị trí. Trong ví dụ này, chúng ta sẽ sử dụng các hàm sin và cos để tạo các vector mã hóa vị trí.

Giả sử chiều nhúng là 3, các vector mã hóa vị trí sẽ được tính như sau:

Cho vị trí 0 (từ đầu tiên):
- PE(0) = [sin(0/10000^0), cos(0/10000^0), sin(0/10000^0)]

Cho vị trí 1 (từ thứ hai):
- PE(1) = [sin(1/10000^1), cos(1/10000^1), sin(1/10000^1)]

Cho vị trí 2 (từ thứ ba):
- PE(2) = [sin(2/10000^0), cos(2/10000^0), sin(2/10000^0)]

Vì sin(0) = 0, sin(1) = 0.8415, sin(2) = 0.9093, cos(0) = 1, cos(1) = 0.5403, cos(2) = -0.4161.

Nên, các vector mã hóa vị trí là:

PE(0) = [0, 1, 0]
PE(1) = [0.8415, 0.5403, 0.8415]
PE(2) = [0.9093, -0.4161, 0.9093]

Để tích hợp mã hóa vị trí, chúng ta cộng vector mã hóa vị trí tương ứng vào mỗi vector nhúng từ:

- Từ "Tôi" với mã hóa vị trí: [0.2, 0.3, -0.1] + [0, 1, 0] = [0.2, 1.3, -0.1]
- Từ "yêu" với mã hóa vị trí: [-0.5, 0.7, 0.2] + [0.8415, 0.5403, 0.8415] =

 [0.3415, 1.2403, 1.0415]
- Từ "mèo" với mã hóa vị trí: [0.7, 0.8, 0.9] + [0.9093, -0.4161, 0.9093] = [1.6093, 0.3839, 1.8093]

Bằng cách cộng các vector mã hóa vị trí vào các vector nhúng từ, chúng ta giới thiệu thông tin về vị trí tương đối của các từ trong chuỗi đầu vào. Điều này cho phép mô hình Transformer nắm bắt thứ tự tuần tự và các phụ thuộc giữa các từ, điều quan trọng cho các nhiệm vụ như dịch máy hoặc phân tích cảm xúc.


## Layer Normalization

Layer Normalization là một kỹ thuật được sử dụng trong các mô hình học sâu để chuẩn hóa các kích hoạt (kết quả chuyển đổi đầu vào thành đầu ra bằng hàm kích hoạt - tạm gọi là các kích hoạt) của các đơn vị trong một lớp. Nó giải quyết vấn đề của sự thay đổi phân phối đầu vào của lớp trong quá trình huấn luyện, gây khó khăn cho quá trình học.


Công thức cho Layer Normalization có thể được biểu diễn như sau:

```
output = scale * (input - mean) / sqrt(variance + epsilon) + bias

```

Ở đây, `đầu vào` đại diện cho các kích hoạt đầu vào của một lớp, `trung bình` và `phương sai` đại diện cho giá trị trung bình và phương sai được tính theo chiều đầu vào, `epsilon` là một hằng số nhỏ được thêm vào để đảm bảo tính ổn định số học, và `scale` và `bias` là các tham số có thể học giúp mô hình điều chỉnh và dịch chuyển các kích hoạt đã được chuẩn hóa.

Layer Normalization được áp dụng độc lập cho mỗi lô dữ liệu (batch), điều này làm cho nó phù hợp cho các nhiệm vụ với kích thước lô nhỏ. Nó đã được chứng minh là hiệu quả trong ổn định quá trình huấn luyện, tăng tốc quá trình hội tụ và cải thiện hiệu suất tổng quát của các mô hình học sâu.

Tổng quát, Layer Normalization giúp giảm sự phụ thuộc vào tỷ lệ của các kích hoạt đầu vào, thúc đẩy việc truyền gradient ổn định và cải thiện động học huấn luyện tổng thể (overall training dynamics - gồm learning rate, gradient, loss rate) của mạng neural. Nó đã được sử dụng rộng rãi trong các lĩnh vực khác nhau, bao gồm xử lý ngôn ngữ tự nhiên, thị giác máy tính và nhận dạng giọng nói.

## MASKING

Giả sử chúng ta có một câu: "Tôi thích chơi bóng đá."

Trong mô hình ngôn ngữ, mục tiêu là dự đoán từ tiếp theo trong ngữ cảnh đã cho. Tuy nhiên, trong quá trình huấn luyện, chúng ta thường không muốn cho mô hình truy cập vào các từ trong tương lai vì nó có thể dẫn đến rò rỉ dữ liệu và dự đoán không thực tế. Vì vậy, chế che được áp dụng.

Để áp dụng cơ chế che, thường được ký hiệu là [MASK], để thay thế một số từ trong chuỗi đầu vào trong quá trình huấn luyện. Trong trường hợp này, chúng ta có thể ngẫu nhiên che một số từ trong câu, dẫn đến:

Câu Đầu Vào (có cơ chế che): *"Tôi thích chơi [MASK] bóng đá."*

Bây giờ, trong quá trình huấn luyện, mục tiêu của mô hình là dự đoán từ bị che dựa trên ngữ cảnh xung quanh. Nó học cách hiểu cấu trúc câu, ý nghĩa và sự phụ thuộc giữa các từ để đưa ra dự đoán chính xác. Mô hình nhận chuỗi đầu vào đã được chỉnh sửa (thêm [MASK]) và cố gắng dự đoán bản gốc, không bị che, ở vị trí đã được che.

Trong quá trình huấn luyện hoặc đánh giá, cơ chế che không được sử dụng và mô hình được cung cấp với toàn bộ chuỗi đầu vào. Nó có thể tạo ra dự đoán cho từ tiếp theo trong chuỗi dựa trên kiến thức đã học từ quá trình huấn luyện.

Cơ chế che giúp mô hình tổng quát tốt và xử lý các trường hợp mà nó gặp phải các từ chưa được nhìn thấy hoặc thiếu. Nó khuyến khích mô hình dựa vào ngữ cảnh có sẵn để đưa ra dự đoán chính xác và cải thiện khả năng hiểu cấu trúc câu.
