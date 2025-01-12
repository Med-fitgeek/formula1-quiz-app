-- Création de la table si elle n'existe pas déjà
CREATE TABLE IF NOT EXISTS questions (
    id SERIAL PRIMARY KEY,
    text TEXT NOT NULL,
    title TEXT NOT NULL,
    image TEXT NOT NULL,
    position INTEGER NOT NULL,
    possibleAnswers JSONB NOT NULL
);

-- Insertion des questions
INSERT INTO questions (text, title, image, position, possibleAnswers) VALUES
('Quelle est l''équipe la plus titrée de l''histoire de la Formule 1 ?', 'Facile', NULL, 1,
    '[
        {"text": "Mercedes", "isCorrect": false},
        {"text": "Red Bull", "isCorrect": false},
        {"text": "Mc Laren", "isCorrect": false},
        {"text": "Ferrari", "isCorrect": true}
    ]'::JSONB),
('Quel pilote détient le record du plus grand nombre de victoires en Formule 1 ?', 'Facile', NULL, 2,
    '[
        {"text": "Michael Schumacher", "isCorrect": false},
        {"text": "Sebastian Vettel", "isCorrect": false},
        {"text": "Lewis Hamilton", "isCorrect": true},
        {"text": "Ayrton Senna", "isCorrect": false}
    ]'::JSONB),
('En quelle année la première course officielle de Formule 1 a-t-elle eu lieu ?', 'Moyen', NULL, 3,
    '[
        {"text": "1946", "isCorrect": false},
        {"text": "1950", "isCorrect": true},
        {"text": "1960", "isCorrect": false},
        {"text": "1975", "isCorrect": false}
    ]'::JSONB),
('Quel est le surnom du circuit de Spa-Francorchamps ?', 'Moyen', NULL, 4,
    '[
        {"text": "LNULLArdenne Bleu", "isCorrect": true},
        {"text": "Le Circuit des Flandres", "isCorrect": false},
        {"text": "La Boucle de Liège", "isCorrect": false},
        {"text": "Le Grand Défi", "isCorrect": false}
    ]'::JSONB),
('Quel pilote légendaire est surnommé "The Professor" ?', 'Facile', NULL, 5,
    '[
        {"text": "Ayrton Senna", "isCorrect": false},
        {"text": "Nigel Mansell", "isCorrect": false},
        {"text": "Alain Prost", "isCorrect": true},
        {"text": "Niki Lauda", "isCorrect": false}
    ]'::JSONB),
('Quelle équipe est la première à avoir remporté un championnat de Formule 1 ?', 'Difficile', NULL, 6,
    '[
        {"text": "Ferrari", "isCorrect": false},
        {"text": "Alfa Romeo", "isCorrect": true},
        {"text": "Lotus", "isCorrect": false},
        {"text": "Cooper", "isCorrect": false}
    ]'::JSONB),
('Quel est le circuit le plus long du calendrier de Formule 1 ?', 'Difficile', NULL, 7,
    '[
        {"text": "Circuit de Monaco", "isCorrect": false},
        {"text": "Suzuka", "isCorrect": false},
        {"text": "Spa-Francorchamps", "isCorrect": true},
        {"text": "Silverstone", "isCorrect": false}
    ]'::JSONB),
('Quel pilote a remporté le plus de pole positions ?', 'Facile', NULL, 8,
    '[
        {"text": "Lewis Hamilton", "isCorrect": true},
        {"text": "Sebastian Vettel", "isCorrect": false},
        {"text": "Michael Schumacher", "isCorrect": false},
        {"text": "Ayrton Senna", "isCorrect": false}
    ]'::JSONB),
('En quelle année Lewis Hamilton a-t-il remporté son premier championnat ?', 'Moyen', NULL, 9,
    '[
        {"text": "2007", "isCorrect": false},
        {"text": "2008", "isCorrect": true},
        {"text": "2009", "isCorrect": false},
        {"text": "2010", "isCorrect": false}
    ]'::JSONB),
('Quel constructeur a introduit la technologie des turbos en Formule 1 ?', 'Difficile', NULL, 10,
    '[
        {"text": "Ferrari", "isCorrect": false},
        {"text": "Renault", "isCorrect": true},
        {"text": "Honda", "isCorrect": false},
        {"text": "BMW", "isCorrect": false}
    ]'::JSONB);


-- Création de la table des participations si elle n'existe pas déjà
CREATE TABLE IF NOT EXISTS participations (
    id SERIAL PRIMARY KEY,
    player_name TEXT NOT NULL,
    score INTEGER NOT NULL
);

-- Insertion des participations
INSERT INTO participations (player_name, score) VALUES
('Alice', 8),
('Bob', 6),
('Charlie', 9);