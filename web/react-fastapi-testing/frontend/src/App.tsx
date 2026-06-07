import { useState } from "react";
import Button from "./components/Button";
import TextField from "./components/TextField";

function App() {
  const [text, setText] = useState("");

  return (
    <>
      <div style={{ display: "flex", gap: "6px" }}>
        <Button>Press to send</Button>
        <TextField
          value={text}
          onChange={setText}
          placeholder="Enter text here..."
        />
      </div>
      <p>{text}</p>
    </>
  );
}

export default App;
