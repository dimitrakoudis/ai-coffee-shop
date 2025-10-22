import secrets

from app.agents import constants
from app.models.menu import Menu


# Not covering with tests, given we'd use a real agent instead.
class Customer:  # pragma: no cover
    def __init__(
        self,
        *,
        number: str,
        menu: Menu,
        next_drink_names: list[str] | None = None,
    ) -> None:
        self._number = number
        self._menu = menu
        self._next_drink_names = next_drink_names or []

    @property
    def number(self) -> str:
        return self._number

    @property
    def next_drink_names(self) -> list[str]:
        return self._next_drink_names

    @next_drink_names.setter
    def next_drink_names(self, value: list[str]) -> None:
        self._next_drink_names = value

    @property
    def menu(self) -> Menu:
        return self._menu

    @menu.setter
    def menu(self, value: Menu) -> None:
        self._menu = value

    @staticmethod
    def _get_word_articled(word: str) -> str:
        """
        Returns a word articled with "a" or "an" depending on its first letter.
        Still not 100% accurate, but good enough for this example.
        Lacks in handling special cases like "an hour", "a user", etc.
        """
        if not word:
            raise ValueError("Word cannot be empty.")

        article = "a"
        if word.lower()[0] in "aeiou":
            article = "an"
        return f"{article} {word}"

    def _pick_a_drink_name(self) -> str | None:
        """Picks either a random menu drink or the predefined next drink."""
        if self._next_drink_names:
            return self._next_drink_names.pop(0)
        all_drinks = [p for p in self._menu.products if p.is_drink]
        if not all_drinks:
            return None
        return secrets.choice(all_drinks).name

    def _get_order_message(self, product_name: str) -> str:
        return (
            f"{constants.I_WOULD_LIKE_MESSAGE} "
            f"{self._get_word_articled(product_name)}."
        )

    @staticmethod
    def _is_message_welcome(message: str) -> bool:
        return message == constants.WELCOME_MESSAGE

    @staticmethod
    def _is_message_i_dont_understand(message: str) -> bool:
        return message == constants.I_DONT_UNDERSTAND_MESSAGE

    @staticmethod
    def _is_message_will_bring_you_the_menu(message: str) -> bool:
        return message == constants.WILL_BRING_YOU_THE_MENU_MESSAGE

    @staticmethod
    def _is_message_product_not_found(message: str) -> bool:
        return message == constants.PRODUCT_NOT_FOUND_MESSAGE

    @staticmethod
    def _is_message_goodbye(message: str) -> bool:
        return constants.GOODBYE_MESSAGE in message

    @staticmethod
    def _is_message_take_your_time(message: str) -> bool:
        return message == constants.TAKE_YOUR_TIME_MESSAGE

    async def handle(self, *, message: str) -> str | None:
        if self._is_message_welcome(
            message
        ) or self._is_message_product_not_found(message):
            drink = self._pick_a_drink_name()
            if not drink:
                return constants.NEED_THE_DRINK_MENU_MESSAGE
            return self._get_order_message(drink)

        if self._is_message_i_dont_understand(message):
            return constants.NEED_MORE_TIME_MESSAGE

        if (
            self._is_message_goodbye(message)
            or self._is_message_take_your_time(message)
            or self._is_message_will_bring_you_the_menu(message)
        ):
            return None

        return constants.THAT_IS_ALL_MESSAGE
