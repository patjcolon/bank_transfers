"""
Contains text stylization features for text color, style, and background
styl for all text style/color/background needs and unstyl to go back to default
suitr is for use in card games. input list of cards ['AD', 'KH'] and it will return them as playing cards
By patjcolon
Last updated 6/28/2023
"""


def unstyl():
    """Resets text style, color, and highlight to default AKA unstyl!
    Currently same in practicality as the defaults of styl(). Will add more unstyl resets as features are added."""
    return "\033[0;39;49m"


def styl(color_choice: str = "Default", style_choice: str = "Reset", highlight_choice: str = "Default") -> str:
    """
    Stylizes text color, style, and highlight. Returns a stylization escape command string.
    Custom variable presets can be made as well as custom print functions
    color_choice and highlight_choice options: 'Default', 'Black', 'Red', 'Green', 'Yellow', 'Blue', 'Magenta', Cyan', 'White'
    style_choice options: 'Reset', 'Bold', 'Dim', 'Italic', 'Underline', 'Blinking', 'Inverse', 'Invisible', 'Strikethrough'
    Style choices can be stacked. must be reset to clear. Default setting resets style.
    """
    text_colors = {"Default": ";39", "Black": ";30", "Red": ";31", "Green": ";32", "Yellow": ";33",
                   "Blue": ";34", "Magenta": ";35", "Cyan": ";36", "White": ";37", }

    text_styles = {"Reset": "\033[0", "Bold": "\033[1", "Dim": "\033[2", "Italic": "\033[3", "Underline": "\033[4",
                   "Blinking": "\033[5", "Inverse": "\033[7", "Invisible": "\033[8", "Strikethrough": "\033[9"}

    text_highlight = {"Default": ";49m", "Black": ";40m", "Red": ";41m", "Green": ";42m", "Yellow": ";43m",
                      "Blue": ";44m", "Magenta": "1;45m", "Cyan": ";46m", "White": ";47m", }

    if not color_choice.isalpha() or not style_choice.isalpha() or not highlight_choice.isalpha():
        return "\033[4;31m \nstylError: styl() argument cannot contain characters outside of the alphabet.\033[0;39m\n"
    color_code = text_colors[color_choice]
    style_code = text_styles[style_choice]
    highlight_code = text_highlight[highlight_choice]

    color_style_code = style_code + color_code + highlight_code
    return color_style_code


def suitr(cards: list = ["LiveD", "LaughC","CodeH"]):
    """suitr is a cardgame helper function that uses styl. it can take any card like 'AD' and turn it into
    a white background card with red/black values and suit"""

    # styl() presets for colorizing cards with a white background
    rst = unstyl()                             # rst:   Reset unstyl()
    reds = styl("Red", "Underline", "White")        # reds:  Red Suits      "Red Bold White"
    blks = styl("Black", "Underline", "White")      # blks:  Black Suits    "Black Bold White"
    # Unicode for suit symbols
    suits = {
    "D": "\u2666",
    "C": "\u2663",
    "H": "\u2665",
    "S": "\u2660",
    }
    
    # turning card input into a card
    card_art = ""
    for card in cards:
        card_value = card[:-1]
        card_suit = card[-1]
        card_color = reds if card_suit == 'D' or card_suit == 'H' else blks
        card_art += f"{card_color} {card_value} {suits[f'{card_suit}']} {rst}, "
    card_art = card_art[:-2]
    return f" {card_art}\033[0K"


# u2620 is skull ☠ w on b, u2622 is radiation ☢ b on y, 2728 is sparkles for win ✨ 2B50⭐
# \u00A2 is cents symbol ¢ b on w or b on , u0024 is dollar $ (dont need code...), 
# u23F4 for hourglass ⏳, u23f0 is alarmclock ⏰, 
# 270A-C is rock-paper-scissors ✊ ✋ ✌