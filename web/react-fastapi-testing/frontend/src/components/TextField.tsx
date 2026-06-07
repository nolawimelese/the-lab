interface TextFieldProps {
  value: string;
  onChange: (value: string) => void;
  placeholder?: string;
}

function TextField({ value, onChange, placeholder }: TextFieldProps) {
  return (
    <input
      type="text"
      value={value}
      onChange={(e) => onChange(e.target.value)}
      placeholder={placeholder}
      style={{
        border: "1px solid black",
        borderRadius: "4px",
        padding: "6px 10px",
        fontSize: "14px",
      }}
    />
  );
}

export default TextField;
