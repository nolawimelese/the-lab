import type { ReactNode } from "react";

interface Props {
  children: ReactNode;
  onClick?: () => void;
}

const Button = ({ children, onClick }: Props) => {
  return (
    <button
      type="button"
      onClick={onClick}
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
