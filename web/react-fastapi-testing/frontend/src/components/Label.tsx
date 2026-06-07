interface LabelProps {
  text: string;
}

function Label({ text }: LabelProps) {
  return (
    <span
      style={{
        border: "1px solid black",
        borderRadius: "999px",
        padding: "2px 10px",
        fontSize: "12px",
      }}
    >
      {text}
    </span>
  );
}

export default Label;
