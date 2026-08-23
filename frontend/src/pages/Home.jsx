import { useState, useEffect } from "react";
import { Upload } from "lucide-react";

import SearchBar from "../components/SearchBar";
import RecentMemories from "../components/RecentMemories";
import PermissionScreen from "../components/PermissionScreen";

import { uploadMemory, getMemories } from "../services/api";

export default function Home() {
  const [granted, setGranted] = useState(
    localStorage.getItem("permission") === "true"
  );

  const [memories, setMemories] = useState([]);
  const [searchResult, setSearchResult] = useState(null);

  const [total, setTotal] = useState(0);
  const [current, setCurrent] = useState(0);
  const [progress, setProgress] = useState(0);

  useEffect(() => {
    if (granted) loadMemories();
  }, [granted]);

  const loadMemories = async () => {
    try {
      const data = await getMemories();
      setMemories(data);
    } catch (err) {
      console.log(err);
    }
  };

  const grantPermission = () => {
    localStorage.setItem("permission", "true");
    setGranted(true);
  };

  const handleUpload = async (e) => {
    const files = Array.from(e.target.files);

    if (!files.length) return;

    try {
      setTotal(files.length);
      setCurrent(0);
      setProgress(0);

      for (let i = 0; i < files.length; i++) {
        await uploadMemory(files[i]);

        const done = i + 1;
        setCurrent(done);
        setProgress(Math.round((done / files.length) * 100));
      }

      await loadMemories();
      alert("🎉 All memories indexed!");
    } catch (err) {
      console.error(err);
      alert("Upload failed");
    }
  };

  if (!granted) {
    return <PermissionScreen onGrant={grantPermission} />;
  }

  return (
    <div className="home">
      {/* HERO */}
      <section className="hero">
        <h1 className="logo">MemoryMine</h1>

        <p className="subtitle">
          Your AI-powered second brain. Search photos, PDFs and chats naturally.
        </p>

        <SearchBar onResult={setSearchResult} />
      </section>

      {/* SEARCH RESULT */}
      {searchResult && (
        <section className="result-card">
          <h3>✨ Memory Found</h3>

          <p className="result-sub">
            Retrieved from your indexed memories
          </p>

          {/* AI Answer */}
          <div className="result-answer">
            {searchResult.answer}
          </div>

          {/* ONLY ONE SOURCE FILE */}
          {searchResult.results?.[0] && (
            <div className="result-file">
              <h4>{searchResult.results[0].filename}</h4>

              <p>
                {searchResult.results[0].text.slice(0, 180)}...
              </p>
            </div>
          )}
        </section>
      )}

      {/* UPLOAD */}
      <section className="upload-section">
        <label className="upload-btn">
          <Upload size={20} />
          Connect Memories

          <input
            type="file"
            hidden
            multiple
            accept=".pdf,.txt,.jpg,.jpeg,.png"
            onChange={handleUpload}
          />
        </label>
      </section>

      {/* PROGRESS */}
      {total > 0 && progress < 100 && (
        <section className="progress-card">
          <h3>Indexing Memories</h3>

          <p>
            {current} of {total} files processed
          </p>

          <div className="progress-bg">
            <div
              className="progress-fill"
              style={{ width: `${progress}%` }}
            />
          </div>

          <strong>{progress}%</strong>
        </section>
      )}

      {/* RECENT MEMORIES */}
      <RecentMemories memories={memories} />
    </div>
  );
}