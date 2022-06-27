import React from "react";
import "../css/Messages.css";

const MessageL = ({ text }) => {
  return (
    <div className="d-flex flex-column gap-2">
      <p className="m-0 messageL p-3 align-self-start ">{text}</p>
      <h6 className="align-self-start">Hachikō</h6>
    </div>
  );
};

export default MessageL;
