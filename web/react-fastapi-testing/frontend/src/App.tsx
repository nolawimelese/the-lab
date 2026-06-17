import React, { useState, useEffect } from "react";
import api from "./api";

/*
import { useState } from "react";
import Button from "./components/Button";
import TextField from "./components/TextField";
*/

function App() {
  const [text, setText] = useState("");
  const [formData, setFormData] = useState({
    message: "",
  });

  const fetchMessages = async () => {
    const response = await api.get("/message");
    setText(response.data);
  };

  useEffect(() => {
    fetchMessages();
  }, []);

  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value, type, checked } = event.currentTarget;
    setFormData((prev) => ({
      ...prev,
      [name]: type === "checkbox" ? checked : value,
    }));
  };

  const handleFormSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    await api.post("/message", formData);
    fetchMessages();
    setFormData({
      message: "",
    });
  };

  /*
  return (
    <>
      <div style={{ display: "flex", gap: "6px" }}>
        <Button onClick={() => text && console.log(text)}>Press to send</Button>
        <TextField
          value={text}
          onChange={setText}
          placeholder="Enter text here..."
        />
      </div>
      <p>{text}</p>
    </>
  );
  */
}

export default App;
