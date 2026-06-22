import React, { useState, useEffect } from "react";
import api from "./api";

/* legacy imports
import { useState } from "react";
import Button from "./components/Button";
import TextField from "./components/TextField";
*/

function App() {
  const [text, setText] = useState<{ id: number; message: string }[]>([]);
  const [formData, setFormData] = useState({
    message: "",
  });
  const [averageLength, setAverageLength] = useState<number>(0);

  const fetchMessages = async () => {
    const response = await api.get("/message/");
    setText(response.data);
  };

  const fetchAverageLength = async () => {
    const response = await api.get("/message/average_length");
    setAverageLength(response.data.avg_length);
  };

  useEffect(() => {
    fetchMessages();
    fetchAverageLength();
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
    await api.post("/message/", formData);
    fetchMessages();
    fetchAverageLength();
    setFormData({
      message: "",
    });
  };

  return (
    <>
      <nav className="navbar navbar-dark bg-primary">
        <div className="container-fluid">
          <a className="navbar-brand" href="#">
            Messager
          </a>
        </div>
      </nav>
      <div className="container">
        <form onSubmit={handleFormSubmit}>
          <div className="mb-3 mt-3">
            <label htmlFor="message" className="form-label">
              Message
            </label>
            <input
              type="text"
              className="form-control"
              id="message"
              name="message"
              value={formData.message}
              onChange={handleInputChange}
            />
          </div>

          <button type="submit" className="btn btn-primary">
            Submit
          </button>
        </form>

        <p className="mt-3">
          Average message length:
          {averageLength > 0
            ? ` ${averageLength} characters`
            : " No messages yet"}
        </p>

        <table className="table table-striped table-bordered">
          <thead>
            <tr>
              <th>ID</th>
              <th>Message</th>
            </tr>
          </thead>
          <tbody>
            {text.map((msg) => (
              <tr key={msg.id}>
                <td>{msg.id}</td>
                <td>{msg.message}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </>
  );

  /* legacy code, just in case I need it later
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
