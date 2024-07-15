from enum import Enum


class Messages(Enum):
    EMPTY_CART_PAGE = "סל הקניות שלך ריק."
    EMPTY_FAV_PAGE = "לא הוספת עדיין פריטים לרשימה"
    COLOR_ERROR = "שדה חובה."
    SIZE_ERROR = "מידה - שדה חובה."
    EMAIL_ERROR =  "אימייל או סיסמה שגויים"