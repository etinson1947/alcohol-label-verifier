```javascript id="react1"
import React, { useState } from "react";
import axios from "axios";

function App() {

  const [file, setFile] = useState(null);
  const [sku, setSku] = useState("");
  const [result, setResult] = useState(null);

  const upload = async () => {

    const form = new FormData();
    form.append("sku", sku);
    form.append("files", file);

    const res = await axios.post(
      "/api/verify",
      form
    );

    setResult(res.data);
  };

  return (
    <div>
      <h1>Label Compliance Dashboard</h1>

      <input
        value={sku}
        onChange={e => setSku(e.target.value)}
        placeholder="SKU"
      />

      <input
        type="file"
        onChange={e => setFile(e.target.files[0])}
      />

      <button onClick={upload}>
        Verify
      </button>

      <pre>
        {JSON.stringify(result, null, 2)}
      </pre>

    </div>
  );
}

export default App;
```
