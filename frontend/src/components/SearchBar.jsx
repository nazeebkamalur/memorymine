import { useState } from "react";
import { Search } from "lucide-react";
import { searchMemory } from "../services/api";

export default function SearchBar({ onResult }) {
  const [query, setQuery] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSearch = async () => {
    if (!query.trim()) return;

    setLoading(true);

    // 🔥 Remove previous search immediately
    onResult(null);

    try {
      const res = await searchMemory(query);
      onResult(res);
    } catch (err) {
      console.error(err);
      alert("Search failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="hero-search">
      <Search className="hero-icon" size={24} />

      <input
        type="text"
        placeholder="Ask anything from your memories..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        onKeyDown={(e) => e.key === "Enter" && handleSearch()}
      />

      <button onClick={handleSearch} disabled={loading}>
        {loading ? "Searching..." : "Search"}
      </button>
    </div>
}