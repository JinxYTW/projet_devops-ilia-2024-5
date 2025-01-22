document.addEventListener("DOMContentLoaded", () => {
  fetchTweets();
});

function fetchTweets() {
  fetch("https://api.example.com/tweetlist") 
    .then((response) => {
      if (!response.ok) {
        throw new Error("Erreur lors de la récupération des tweets");
      }
      return response.json();
    })
    .then((data) => {
      displayTweets(data.tweets);
    })
    .catch((error) => {
      console.error("Erreur:", error);
    });
}

function displayTweets(tweets) {
  const zoneTweets = document.getElementById("zoneTweets");

  zoneTweets.innerHTML = "";

  tweets.forEach((tweet) => {
    const tweetDiv = document.createElement("div");
    tweetDiv.classList.add("tweet");

    const tweetAuthor = document.createElement("h3");
    tweetAuthor.textContent = `@${tweet.autor}`;

    const tweetMessage = document.createElement("p");
    tweetMessage.textContent = tweet.message;

    const zoneInterraction = document.createElement("div");
    zoneInterraction.id = "zoneInterraction";

    const likeButton = createInteractionButton("../../data/coeur.png");
    const commentButton = createInteractionButton("../../data/commentaire.jpeg");
    const shareButton = createInteractionButton("../../data/partage.png");

    zoneInterraction.appendChild(likeButton);
    zoneInterraction.appendChild(commentButton);
    zoneInterraction.appendChild(shareButton);

    tweetDiv.appendChild(tweetAuthor);
    tweetDiv.appendChild(tweetMessage);
    tweetDiv.appendChild(zoneInterraction);

    tweetDiv.addEventListener("click", () => {
      window.location.href = "./conversations.html";
    });

    zoneTweets.appendChild(tweetDiv);
  });
}

function createInteractionButton(iconPath) {
  const button = document.createElement("button");
  const img = document.createElement("img");
  img.src = iconPath;
  img.style.width = "15px";
  img.style.height = "15px";
  button.appendChild(img);
  return button;
}
