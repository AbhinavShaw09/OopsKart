import { useState, useEffect } from "react";
import { useAuth } from "../context/AuthContext";

export const useFetch = (url) => {
  const { token } = useAuth();
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(url, {
          headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "application/json",
          },
        });
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        const result = await response.json();
        setData(result);
      } catch (error) {
        setError(error);
        console.error("Fetch error:", error);
      } finally {
        setLoading(false);
      }
    };
    if (token) {
      fetchData();
    }
  }, [url, token]);

  return { data, loading, error };
};
