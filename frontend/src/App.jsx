import { useState } from "react";

function App() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([]);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage = { role: "user", text: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput("");

    try {
      const res = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: input }),
      });

      const data = await res.json();
      setMessages((prev) => [
        ...prev,
        { role: "assistant", text: data.reply },
      ]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        { role: "assistant", text: "Помилка: сервер не відповідає" },
      ]);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center p-4">
      <h1 className="text-2xl font-bold mb-4">Жартівливий бот</h1>

      <div className="w-full max-w-xl bg-white rounded-xl shadow p-4 mb-4 overflow-y-auto h-[60vh]">
        {messages.map((msg, idx) => (
          <div key={idx} className="mb-2">
            <strong className={msg.role === "user" ? "text-blue-600" : "text-green-600"}>
              {msg.role === "user" ? "Ти:" : "Бот:"}
            </strong>{" "}
            {msg.text}
          </div>
        ))}
      </div>

      <div className="w-full max-w-xl flex gap-2">
        <input
          className="flex-1 p-2 border rounded-lg"
          type="text"
          value={input}
          placeholder="Введи повідомлення..."
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && sendMessage()}
        />
        <button
          onClick={sendMessage}
          className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition"
        >
          Надіслати
        </button>
      </div>
    </div>
  );
}

export default App;
