import { Upload } from "lucide-react";

export default function UploadButton({ onUpload }) {
  return (
    <label className="upload-btn">
      <Upload size={18} />
      Connect Memories

      <input
        hidden
        multiple
        type="file"
        accept=".pdf,.txt,.jpg,.jpeg,.png"
        onChange={(e) => onUpload(e.target.files)}
      />
    </label>
  );
}