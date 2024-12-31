from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Happy New Year 2025!</title>
      <style>
        body {
          font-family: Arial, sans-serif;
          text-align: center;
          background: linear-gradient(135deg, #ff9a8b, #fad0c4);
          color: white;
          height: 100vh;
          margin: 0;
          display: flex;
          align-items: center;
          justify-content: center;
          flex-direction: column;
        }

        .shop-name {
          font-size: 2rem;
          font-weight: bold;
          margin-top: 20px;
          color: #ff6f61;
          text-transform: uppercase;
          letter-spacing: 2px;
        }

        .image-container {
          margin-bottom: 30px;
          margin-top: 20px;
        }

        img {
          width: 250px;  /* Set a width for the image */
          height: auto;
          border-radius: 10px;  /* Optional: makes the image circular */
          box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);  /* Optional: adds shadow to the image */
        }
        


        .container {
          text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
        }

        button {
          background-color: #ff6f61;
          color: white;
          border: none;
          padding: 10px 20px;
          font-size: 1rem;
          cursor: pointer;
          border-radius: 5px;
          margin-top: 20px;
          box-shadow: 2px 2px 6px rgba(0, 0, 0, 0.2);
          transition: transform 0.2s ease, background 0.3s ease;
        }

        button:hover {
          background-color: #e65550;
          transform: scale(1.05);
        }
      </style>
    </head>
    <body>
      <div class="image-container">
        <!-- Image path should be correct -->
        <img src="static/images/ayyapareadymades.jpg" alt="Shop Image">

      </div>
      <div class="shop-name">Ayyapa Readymades</div>
      <div class="container">
        <h1>🎉 Happy New Year 2025! 🎆</h1>
        <p id="message">Wishing you joy, success, and love in 2025!</p>
        <button onclick="changeMessage()">Click for a New Wish!</button>
      </div>
      <script>
        function changeMessage() {
          const messages = [
            "🌟 May 2025 bring you endless happiness!",
            "🎆 Here's to new opportunities in 2025!",
            "✨ Shine brighter than ever in 2025!",
            "🌈 Make this year unforgettable!",
            "🎉 Happy New Year 2025! Cheers to success!"
          ];
          const randomMessage = messages[Math.floor(Math.random() * messages.length)];
          document.getElementById("message").innerText = randomMessage;
        }
      </script>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
