USE polytex;

CREATE TABLE utilisateur (
    Nom VARCHAR(50) NOT NULL,
    Prenom VARCHAR(50) NOT NULL,
    Email VARCHAR(100) NOT NULL,
    Mot_de_passe VARCHAR(255) NOT NULL,
    Nom_utilisateur VARCHAR(50) NOT NULL PRIMARY KEY,
    Pseudo VARCHAR(50) NOT NULL
);

INSERT INTO utilisateur (Nom, Prenom, Email, Mot_de_passe, Nom_utilisateur, Pseudo)
VALUES
    ('Dupont', 'Jean', 'jean.dupont@example.com', '$2y$10$nrDWDpEgOI0JrMVZs00rrOsnD/dALCYn3T4nKWIX3EyrpNMF81TSe', 'jdupont', 'JeanD'),
    ('Martin', 'Sophie', 'sophie.martin@example.com', '$2y$10$nrDWDpEgOI0JrMVZs00rrOsnD/dALCYn3T4nKWIX3EyrpNMF81TSe', 'smartin', 'SophieM'),
    ('Durand', 'Luc', 'luc.durand@example.com', '$2y$10$nrDWDpEgOI0JrMVZs00rrOsnD/dALCYn3T4nKWIX3EyrpNMF81TSe', 'ldurand', 'LucD'),
    ('Moreau', 'Claire', 'claire.moreau@example.com', '$2y$10$nrDWDpEgOI0JrMVZs00rrOsnD/dALCYn3T4nKWIX3EyrpNMF81TSe', 'cmoreau', 'ClaireM'),
    ('Rousseau', 'Paul', 'paul.rousseau@example.com', '$2y$10$nrDWDpEgOI0JrMVZs00rrOsnD/dALCYn3T4nKWIX3EyrpNMF81TSe', 'prousseau', 'PaulR');
