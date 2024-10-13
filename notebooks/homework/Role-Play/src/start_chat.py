from utils import ChatUtils


def add_history(history, role, content ):
    message = {"role":role,"content":content}
    history.append(message)

def start_chat(chat,history,meta_data,user_content):
    if user_content:
        add_history(history,"user",user_content)

    assistant_reply = chat(meta_data,history)
    add_history(history,"assistant",assistant_reply)
    return assistant_reply


def start():

    chatUtils  = ChatUtils()
    li_meta_data, li_history, ye_meta_data, ye_history,start_message,iteration_num= chatUtils.get_info()
    
    
    chat = chatUtils.start_chat
    user_content = start_message
    flag = True
    for _ in range(iteration_num):
        
        if flag:
            user_content = start_chat(chat,li_history,li_meta_data,user_content)
            print(f"李白: {user_content}")
        else:
             user_content = start_chat(chat,ye_history,ye_meta_data,user_content)
             print(f"叶瑶: {user_content}")

        flag = False if flag else True

if __name__ == '__main__':
    start()