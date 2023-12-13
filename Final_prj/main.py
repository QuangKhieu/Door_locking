from Com import com_serial
from Server_getdata import get_data
from STT_TTS import stt_tts
import  user_Checking as uC
import time

if __name__ == '__main__':
    id = com_serial.atp_seial('COM3', 9600)
    print(id)
    # id = 3
    data = get_data.get_data(int(id))
    print(data)
    list_info = data[2:9]
    person1 = uC.UserChecking(list_info)
    fence = person1.chosen_fence
    print(fence)
    stt_tts.text_to_speech('Hãy trả lời')
    stt_tts.text_to_speech(fence['question'])
    # # #
    # # #
    answer = stt_tts.speech_to_text()
    check = person1.checkk(answer)
    print(answer)
    if check >= 0.5:
        com_serial.pta_serial("COM3", 9600)
    #     print("yes")
    # print(check)
    # com_serial.pta_serial("COM3", 9600)
    # time.sleep(2)
    #com_serial.pta_serial("COM3", 9600)



