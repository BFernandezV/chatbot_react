import React from "react";
import "../css/Messages.css";

const MessageR = ({ text }) => {
  return (
    <div className="d-flex flex-column gap-2">
      <p className="m-0 messageR p-3 align-self-end">{text}</p>
      <h6 className="align-self-end">Tú</h6>
    </div>
  );
};

export default MessageR;
