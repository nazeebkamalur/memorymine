import { FileText, MessageCircle, Image } from "lucide-react";

export default function RecentMemories({ memories }) {
  const sortedMemories = [...memories].sort(
    (a, b) => new Date(b.timestamp) - new Date(a.timestamp)
  );

  return (
    <section className="recent-section">
      <h2>Recent Memories</h2>

      <div className="memory-grid">
        {sortedMemories.map((m) => (
          <div className="memory-card" key={m.id}>
            <div className="icon">
              {m.source_type === "whatsapp" && (
                <MessageCircle color="#16A34A" size={26} />
              )}
              {m.source_type === "pdf" && (
                <FileText color="#DC2626" size={26} />
              )}
              {m.source_type === "image" && (
                <Image color="#EA580C" size={26} />
              )}
            </div>

            <h3>{m.filename}</h3>

            <p>{m.text.substring(0, 80)}...</p>

            <span>{m.source_type}</span>
          </div>
        ))}
      </div>
    </section>
  );
}