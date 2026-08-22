import { Shield, FileText, Image, MessageCircle } from "lucide-react";

export default function PermissionScreen({ onGrant }) {
  return (
    <div className="permission-page">
      <div className="permission-card">
        <Shield size={60} color="#2563EB" />

        <h1>Connect Your Memories</h1>

        <p>
          Grant one-time permission to securely index your Photos, PDFs and
          WhatsApp exports.
        </p>

        <div className="permission-grid">
          <div className="perm-box">
            <MessageCircle size={32} color="#16A34A" />
            <h4>WhatsApp</h4>
            <span>Chat exports</span>
          </div>

          <div className="perm-box">
            <FileText size={32} color="#DC2626" />
            <h4>PDFs</h4>
            <span>Documents</span>
          </div>

          <div className="perm-box">
            <Image size={32} color="#EA580C" />
            <h4>Photos</h4>
            <span>OCR Images</span>
          </div>
        </div>

        <button className="grant-btn" onClick={onGrant}>
          Grant Permission
        </button>
      </div>
    </div>
  );
}