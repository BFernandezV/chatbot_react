import React, { useState, useEffect, useRef } from "react";
import Actions from "./Actions";
import ProfileBot from "./ProfileBot";
import "../css/BodyChat.css";
import Send from "../images/send.png";
import MessageL from "./MessageL";
import MessageR from "./MessageR";
import { LeapFrog } from "@uiball/loaders";

const chatBody = () => {
  const messagesEndRef = useRef(null);

  const [maxId, setMaxId] = useState(1);
  const [textSend, setTextSend] = useState("");
  const [arrayMsg, setArrayMsg] = useState([]);
  const [loader, setLoader] = useState(false);

  useEffect(() => {
    scrollToBottom();
  }, [arrayMsg]);

  const handleChange = (event) => {
    const { value } = event.target;
    setTextSend(value);
  };

  const scrollToBottom = () => {
    messagesEndRef.current.scrollIntoView({ behavior: "smooth" });
  };

  const sendData = () => {
    setLoader(true);
    document.querySelector(".bodyInput__input").value = "";
    connectBot();
  };

  const connectBot = () => {
    fetch("http://localhost:5005/webhooks/rest/webhook", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
        charset: "UTF-8",
      },
      credentials: "same-origin",
      body: JSON.stringify({ sender: "Benjamin", message: textSend }),
    })
      .then((response) => response.json())
      .then((response) => {
        const temp = response;
        let arrayMsgHachi = [];

        console.log("La respuesta del bot: ", temp);
        let value = maxId;
        const idmsg = maxId;

        temp.map((element) => {
          let idElement = value + 1;
          console.log(temp[temp.length - 1] === element);
          arrayMsgHachi.push({
            id: idElement,
            text: element["text"],
            type: "hachiko",
            label: temp[temp.length - 1] === element ? true : false,
          });
          value++;
        });

        setTimeout(function() {
          setArrayMsg([
            ...arrayMsg,
            { id: idmsg, text: textSend, type: "me" },
            ...arrayMsgHachi,
          ]);
          setMaxId(maxId + temp.length + 1);
          setLoader(false);
        }, 1500);
      });
  };

  const sendWithEnter = (event) => {
    if (event.keyCode === 13) {
      sendData();
    }
  };

  return (
    <div className="container-fluid shadow">
      <div className="row">
        <div className="col-12 d-flex bodyNavBar rounded-top">
          <ProfileBot />
          <Actions />
        </div>
        <div className="bodyChat text-secondary d-flex flex-column w-100 px-5 py-4 gap-3 overflow-auto">
          {arrayMsg.length > 0
            ? arrayMsg.map((msg) =>
                msg.type === "me" ? (
                  <MessageR key={msg.id} text={msg.text} />
                ) : (
                  <MessageL key={msg.id} text={msg.text} label={msg.label} />
                )
              )
            : "No hay mensajes"}
          <div ref={messagesEndRef} />
        </div>
        <div className="loader">
          <div
            className={
              (loader ? "visible" : "invisible") +
              " text-center d-flex justify-content-center"
            }
          >
            <LeapFrog size={50} speed={2.5} color="white" />
          </div>
        </div>

        <div className="bodyInput rounded-bottom">
          <div className="d-flex gap-3 p-3">
            <input
              type="text"
              className="form-control bodyInput__input"
              placeholder="Escribe un mensaje para Hachikō"
              aria-describedby="basic-addon1"
              onChange={(event) => handleChange(event)}
              onKeyUp={(event) => sendWithEnter(event)}
            />
            <div className="bodyInput__img h-100">
              <img src={Send} className="img-fluid" onClick={sendData}></img>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default chatBody;
