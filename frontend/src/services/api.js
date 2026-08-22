import axios from "axios";

const API = "http://127.0.0.1:8000";

export const uploadMemory = async (file) => {
  const formData = new FormData();
  formData.append("file", file);

  const res = await axios.post(`${API}/upload`, formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });

  return res.data;
};

export const getMemories = async () => {
  const res = await axios.get(`${API}/memories`);
  return res.data;
};

export const askMemory = async (question) => {
  const res = await axios.post(`${API}/chat`, { question });
  return res.data;
};