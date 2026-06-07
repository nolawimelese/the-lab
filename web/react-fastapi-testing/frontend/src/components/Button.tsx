import type { ReactNode } from "react";

interface Props {
  children: ReactNode;
}

const Button = ({ children }: Props) => {
  return (
    <button
      type="button"
      style={{
        border: "1px solid black",
        borderRadius: "999px",
        padding: "2px 10px",
        fontSize: "12px",
        background: "none",
        cursor: "pointer",
      }}
    >
      {children}
    </button>
  );
};

export default Button;
