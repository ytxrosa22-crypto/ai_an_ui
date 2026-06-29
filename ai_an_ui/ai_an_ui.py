import os
import time
from google import genai
from google.genai import types

# 1. Cấu hình API Key và khởi tạo Client
API_KEY = "AQ.Ab8RN6K844gdQNNWaHBzMB8-H6fnpH5nuZur-Kli4xEr2rfYZg"
client = genai.Client(api_key=API_KEY)

# 2. Thiết lập tính cách và cách hành xử cho AI Piroh
cau_hinh_ai = types.GenerateContentConfig(
    system_instruction=(
        "Bạn là một người bạn tri kỷ ảo vô cùng ấm áp và tinh tế tên là Piroh. "
        "Nhiệm vụ của bạn là lắng nghe, xoa dịu và an ủi người dùng. "
        "Luôn xưng hô thân mật là tớ - cậu. Trả lời ngắn gọn, tự nhiên, Gen Z một chút, "
        "không dùng icon quá đà và tuyệt đối không lặp lại lý thuyết suông."
    ),
    temperature=0.7
)

# 3. Khởi tạo phiên trò chuyện (Giúp AI tự động nhớ lịch sử hội thoại)
chat_session = client.chats.create(model="gemini-2.5-flash", config=cau_hinh_ai)

# Bắt đầu giao diện trò chuyện trên Terminal
print("🤖 AI Piroh: Chào cậu, tớ đã sẵn sàng lắng nghe cậu rồi đây! 🧸\n")

while True:
    # Nhận tin nhắn từ người dùng
    user_input = input("👱 Bạn: ")
    
    # Kiểm tra điều kiện thoát
    if user_input.lower() in ["tạm biệt", "bye", "thoát"]:
        print("\n🤖 AI Piroh: Tạm biệt cậu nhé. Khi nào buồn cứ tìm tớ, tớ luôn ở đây! 🤍")
        break
        
    # Nếu bấm Enter trống thì bỏ qua
    if not user_input.strip():
        continue
        
    try:
        # Thay vì send_message thông thường, ta dùng send_message_stream
        response = chat_session.send_message_stream(user_input)
        
        print("🤖 AI Piroh: ", end="", flush=True)
        for chunk in response:
            print(chunk.text, end="", flush=True)
        print("\n") # Xuống dòng khi chạy xong câu
        
    except Exception as e:
        print(f"❌ [LỖI HỆ THỐNG THỰC TẾ]: {e}\n")
        
    except Exception as e:
        # In lỗi thực tế ra màn hình để debug nếu gặp sự cố mạng
        print(f"❌ [LỖI HỆ THỐNG THỰC TẾ]: {e}\n")
        print("🤖 AI Piroh: Ôi, hình như đường truyền hơi bận một chút... 🤍\n")