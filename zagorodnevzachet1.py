import tkinter as tk  # Импортируем библиотеку tkinter для создания графического интерфейса
import math  # Импортируем библиотеку math для математических расчетов

# Константы
WIDTH, HEIGHT = 800, 600  # Размеры окна приложения
G = 9.81  # Ускорение свободного падения (м/с²)
DEFAULT_DENSITY = 1000  # Плотность воды (кг/м³)

class WaterPumpSimulation:
    def __init__(self, root):
        """Инициализация симуляции водяного насоса."""
        self.root = root  # Сохраняем ссылку на главное окно
        self.root.title("Симуляция работы водяного насоса")  # Устанавливаем заголовок окна

        # Создание холста для рисования
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)  # Создаем холст с заданными размерами
        self.canvas.pack()  # Размещаем холст в главном окне

        # Элементы управления
        control_frame = tk.Frame(root)  # Создаем фрейм для элементов управления
        control_frame.pack()  # Размещаем фрейм в главном окне

        # Слайдер для плотности воды
        tk.Label(control_frame, text="Плотность воды (кг/м³):").pack(side=tk.LEFT)  # Метка для слайдера
        self.density_slider = tk.Scale(control_frame, from_=500, to=1500, resolution=10,
                                       orient=tk.HORIZONTAL, label="Плотность", length=200)
        self.density_slider.set(DEFAULT_DENSITY)  # Устанавливаем начальное значение плотности
        self.density_slider.pack(side=tk.LEFT)  # Размещаем слайдер в фрейме

        # Спинбокс для высоты подъема воды
        tk.Label(control_frame, text="Высота подъема (м):").pack(side=tk.LEFT)  # Метка для спинбокса
        self.height_spinbox = tk.Spinbox(control_frame, from_=0, to=20, increment=1,
                                         width=5)  # Создаем спинбокс для выбора высоты
        self.height_spinbox.pack(side=tk.LEFT)  # Размещаем спинбокс в фрейме

        # Слайдер для давления воды в системе
        tk.Label(control_frame, text="Давление (Па):").pack(side=tk.LEFT)  # Метка для слайдера давления
        self.pressure_slider = tk.Scale(control_frame, from_=0, to=500000, resolution=1000,
                                        orient=tk.HORIZONTAL, label="Давление", length=200)
        self.pressure_slider.set(0)  # Устанавливаем начальное значение давления
        self.pressure_slider.pack(side=tk.LEFT)  # Размещаем слайдер в фрейме

        # Кнопки управления
        tk.Button(control_frame, text="Запустить", command=self.start_animation).pack(side=tk.LEFT)  # Кнопка запуска анимации
        tk.Button(control_frame, text="Сбросить", command=self.reset_simulation).pack(side=tk.LEFT)  # Кнопка сброса параметров

        # Переменные состояния
        self.running = False  # Флаг состояния анимации (работает или нет)
        self.water_level = HEIGHT - 50  # Начальный уровень воды в резервуаре

    def start_animation(self):
        """Запускает анимацию."""
        if not self.running:  # Если анимация не запущена
            self.running = True  # Устанавливаем флаг запущенной анимации
            self.animate()  # Запускаем метод анимации

    def reset_simulation(self):
        """Сбрасывает параметры и останавливает насос."""
        self.running = False  # Останавливаем анимацию
        self.canvas.delete("all")  # Очищаем холст от всех объектов
        self.water_level = HEIGHT - 50  # Сброс уровня воды в резервуаре
        self.pressure_slider.set(0)  # Сброс давления на ноль

    def animate(self):
        """Анимация движения воды."""
        if not self.running:  # Если анимация не запущена, выходим из метода
            return

        # Получение значений из элементов управления
        density = self.density_slider.get()  # Получаем плотность воды из слайдера
        height = int(self.height_spinbox.get())  # Получаем высоту подъема из спинбокса
        pressure = self.pressure_slider.get()  # Получаем давление из слайдера

        # Расчет скорости потока по уравнению Бернулли
        if density > 0:
            v = math.sqrt(2 * pressure / density + 2 * G * height)  # Расчет скорости потока

            # Движение воды вверх к резервуару
            if self.water_level > HEIGHT - height - 50:  # Если уровень воды ниже резервуара
                self.water_level -= v * 0.1  # Уменьшаем уровень воды на основе скорости потока

            if self.water_level < HEIGHT - height - 50:
                self.water_level = HEIGHT - height - 50

            # Отображение уровня воды в резервуаре
            self.canvas.delete("all")

            reservoir_top = HEIGHT - height - 50
            reservoir_bottom = HEIGHT - 50

            self.canvas.create_rectangle(100, reservoir_top,
                                         300, reservoir_bottom,
                                         fill="lightblue", outline="black")
            water_height = max(reservoir_top + height - (HEIGHT - self.water_level), reservoir_top)
            self.canvas.create_rectangle(100, water_height,
                                         300, reservoir_bottom,
                                         fill="blue", outline="black")

            # Запланировать следующий шаг анимации через короткий промежуток времени
            self.root.after(100, self.animate)


# Создание основного окна и запуск приложения
if __name__ == "__main__":
    root = tk.Tk()
    app = WaterPumpSimulation(root)
    root.mainloop()
