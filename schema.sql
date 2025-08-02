CREATE TABLE Movies (
    id INT PRIMARY KEY,
    title NVARCHAR(255),
    director NVARCHAR(255),
    distributor NVARCHAR(255),
    release_date DATE,
    image_url NVARCHAR(500),
    summary NVARCHAR(MAX)
);

CREATE TABLE Comments (
    id INT IDENTITY PRIMARY KEY,
    movie_id INT,
    comment NVARCHAR(MAX),
    likes INT DEFAULT 0,
    dislikes INT DEFAULT 0,
    created_at DATETIME DEFAULT GETDATE()
);