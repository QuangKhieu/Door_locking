from Com import com_serial
from Server_getdata import get_data
from STT_TTS import stt_tts
import  user_Checking as uC
import time




if __name__ == '__main__':
    # id = com_serial.atp_seial('COM3', 9600)
    data = get_data.get_data(5)

    # person1 = uC.UserChecking(list_info=[2002, "Thái Bình", "q1", "a1", "q2", "a2", "q3", "a3"])
    # fence = person1.chosen_fence
    # print(fence['question'])
    #
    #
    # stt_tts.text_to_speech('Hãy trả lời đúng hoặc sai')
    #
    # stt_tts.text_to_speech('alo')
    # answer = stt_tts.speech_to_text()
    # print(answer.lower())
    # print(person1.check(answer.lower()))

    # id = com_serial.atp_seial('COM3', 9600)
    # com_serial.pta_serial('COM3', 9600)



