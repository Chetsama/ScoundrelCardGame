# ScoundrelCardGame

ScoundrelCardGame is a terminal-based card game where players use strategy to defeat monsters, heal, and equip weapons. The game is played with a custom deck of cards, and the goal is to survive and defeat all challenges.

## How to Play

- **Objective**: Survive by managing your health, defeating monsters, and using your cards wisely.
- **Controls**:
  - Use `A`, `B`, `C`, or `D` to select a card from your hand.
  - Use `S` to skip your turn (only allowed with a full hand).
- **Card Types**:
  - **♤♧ (Spades & Clubs)**: Monsters that deal damage.
  - **♡ (Hearts)**: Healing cards to restore health.
  - **♢ (Diamonds)**: Equipable weapons to fight monsters.

## Features

- **Dynamic Gameplay**: Cards are shuffled and dealt randomly, ensuring a unique experience every time.
- **Health Management**: Players start with 20 health points and must avoid reaching 0.
- **Strategic Decisions**: Decide when to heal, equip weapons, or attack monsters.

## To Run 
The docker image can be found here https://hub.docker.com/r/chetsama/scoundrel-card-game

```
docker run -it chetsama/scoundrel-card-game
```
