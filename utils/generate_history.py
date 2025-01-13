def generate_history(messages):
  """messagesの値を元にgemini api用のhistoryを生成する
  
  Args:
    messages (list): streamlitのsession_state.messagesの値

  Returns:
    list: gemini api用のhistory
  """

  history = []
  for message in messages:
    if message["role"] == "user":
      history.append({"role": "user", "parts": message["content"]})
    elif message["role"] == "assistant":
      history.append({"role": "model", "parts": message["content"]})
  return history