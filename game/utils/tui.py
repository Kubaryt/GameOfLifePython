import threading
from copy import deepcopy
from time import sleep

from rich.console import Console
from rich.live import Live

from game.utils.map import Map


def prepare_display(game_map: Map, state: dict) -> str:
    display_str = ""
    display_str += (
        f"Generation: {game_map.generation} Population: {game_map.population}"
        f" Press (p/r/q) to pause/restart game/quit.\n"
    )
    if state["paused"]:
        display_str += "Paused\n\n"
    else:
        display_str += "\n"

    display_str += str(game_map)

    return display_str


def detect_key_input(state: dict, lock):
    from pynput import (
        keyboard,  # todo: fix this, this is placed here to avoid errors when running tests on github actions
    )

    def on_press(key):
        try:
            if key.char == "p":
                with lock:
                    state["paused"] = not state["paused"]
            elif key.char == "r":
                with lock:
                    state["restart"] = True
            elif key.char == "q":
                with lock:
                    state["quit"] = True
                return
        except AttributeError:
            pass

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


def run(game_map: Map):
    console = Console()
    starting_map = deepcopy(game_map)
    state = {"paused": False, "restart": False, "quit": False}
    lock = threading.Lock()

    key_listener = threading.Thread(target=detect_key_input, args=(state, lock), daemon=True)
    key_listener.start()

    with Live(prepare_display(game_map, state), refresh_per_second=5, console=console) as live:
        while game_map.population > 0:
            with lock:
                if state["quit"]:
                    return
                if state["restart"]:
                    game_map = deepcopy(starting_map)
                    live.update(prepare_display(game_map, state))
                    state["restart"] = False

                if not state["paused"]:
                    game_map.next_generation()

                live.update(prepare_display(game_map, state))
                sleep(0.1)
