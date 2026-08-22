import { useState } from "react";
import { Search } from "lucide-react";
import { askMemory } from "../services/api";

export default function SearchBar({ onResult }) {
  const [query, setQuery] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSearch = async () => {
    if (!query.trim()) return;

    setLoading(true);

    try {
      const data = await askMemory(query);

      // Send result to Home.jsx
      if (onResult) onResult(data);
    } catch (err) {
      console.error(err);
      alert("Search failed");
    }

    setLoading(false);
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter") {
      handleSearch();
    }
  };

  return (
    <div className="search-bar">
      <Search size={22} className="search-icon" />

      <input
        type="text"
        placeholder="Where is my prescription from Mom?"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        onKeyDown={handleKeyDown}
      />

      <button onClick={handleSearch} disabled={loading}>
        {loading ? "Searching..." : "Search"}
      </button>
    </div>
  );
}