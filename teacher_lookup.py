import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd

# ── 데이터 ──────────────────────────────────────────────
DATA = [
    ("국어", "허재봉", "진로진학실", "월,화,수,목,금"),
    ("국어", "이진주", "학생인성부실", "월,화,수,목,금"),
    ("국어", "권히재", "1층 본교무실", "월,화,수,목,금"),
    ("국어", "김민정", "4층 2학년 교무실", "월,화,수,목,금"),
    ("수학", "조미선", "1층 본교무실", "월,화,수,목,금"),
    ("수학", "손주희", "1층 본교무실", "월,화,수,목,금"),
    ("수학", "권영철", "4층 2학년 교무실", "월,화,수,목,금"),
    ("수학", "김탁종", "4층 2학년 교무실", "월,화,수,목,금"),
    ("수학", "차지영", "1층 본교무실", "월,화,수,목,금"),
    ("과학(물리)", "손원옥", "4층 1학년 교무실", "월,화,수,목,금"),
    ("과학(물리)(심리)", "이광수", "1층 본교무실", "월,화,수,목,금"),
    ("과학(화학)", "김경희", "1층 본교무실", "월,화,수,목,금"),
    ("과학(화학)", "권규리", "1층 본교무실", "월,화,수,목,금"),
    ("수학", "현희정", "4층 1학년 교무실", "월,화,수,목,금"),
    ("과학(생물)", "이재숙", "4층 2학년 교무실", "월,화,수,목,금"),
    ("과학(생물)", "최미숙", "1층 본교무실", "월,화,수,목,금"),
    ("과학(생물)", "이정현", "1층 본교무실", "월,화,수,목,금"),
    ("과학(지구과학)", "김경민", "교육 정보실", "월,화,수,목,금"),
    ("교무실무원", "조혜정", "1층 본교무실", "월,화,수,목,금"),
    ("특수", "주수연", "1층 본교무실", "월,화,수,목,금"),
    ("일본어", "강다희", "1층 본교무실", "월,화,수,목,금"),
    ("역사", "권순화", "1층 본교무실", "월,화,수,목,금"),
    ("사회(지리)", "송유빈", "4층 2학년 교무실", "월,화,수,목,금"),
    ("사회(일반사회)", "곽은미", "4층 2학년 교무실", "월,화,수,목,금"),
    ("영어", "노지원", "4층 2학년 교무실", "월,화,수,목,금"),
    ("영어", "심규태", "4층 2학년 교무실", "월,화,수,목,금"),
    ("사회(일반사회)", "이화영", "1층 본교무실", "월,화,수,목,금"),
    ("국어", "김성훈", "1층 본교무실", "월,화,수,목,금"),
    ("기술가정", "박은경", "1층 본교무실", "월,화,수,목,금"),
    ("한문(심리)", "최진영", "1층 본교무실", "월,화,수,목,금"),
    ("영어", "장효정", "4층 1학년 교무실", "월,화,수,목,금"),
    ("미술", "박현지", "4층 1학년 교무실", "월,화,수,목,금"),
    ("사회(일반사회)", "최은희", "4층 1학년 교무실", "월,화,수,목,금"),
    ("영어", "정미숙", "4층 1학년 교무실", "월,화,수,목,금"),
    ("음악", "권정현", "4층 1학년 교무실", "월,화,수,목,금"),
    ("사회(지리)", "김경희", "4층 1학년 교무실", "월,화,수,목,금"),
    ("역사", "서은영", "4층 1학년 교무실", "월,화,수,목,금"),
    ("진로", "백윤용", "진로진학실", "월,화,수,목,금"),
]

df = pd.DataFrame(DATA, columns=["과목", "성함", "위치", "근무요일"])
df["과목"] = df["과목"].str.strip()
df["성함"] = df["성함"].str.strip()

SUBJECTS = sorted(df["과목"].unique().tolist())

# ── 색상 ─────────────────────────────────────────────────
BG       = "#f4f6fb"
CARD_BG  = "#ffffff"
PRIMARY  = "#3a6fd8"
TEXT     = "#1e2a3a"
SUBTLE   = "#6b7a99"
BORDER   = "#dce3f0"
ACCENT   = "#e8f0fe"
BTN_FG   = "#ffffff"
ROW_ALT  = "#f0f4ff"

FONT     = "맑은 고딕"

# ── 앱 ───────────────────────────────────────────────────
class TeacherApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("선생님 찾기")
        self.geometry("760x560")
        self.configure(bg=BG)
        self.resizable(True, True)
        self._build()

    # ── UI 구성 ──────────────────────────────────────────
    def _build(self):
        # 헤더
        hdr = tk.Frame(self, bg=PRIMARY, pady=18)
        hdr.pack(fill="x")
        tk.Label(hdr, text="🏫  선생님 찾기", font=(FONT, 18, "bold"),
                 bg=PRIMARY, fg=BTN_FG).pack()
        tk.Label(hdr, text="과목 또는 성함으로 검색하세요",
                 font=(FONT, 10), bg=PRIMARY, fg="#c8d8f8").pack()

        # 검색 카드
        card = tk.Frame(self, bg=CARD_BG, bd=0, relief="flat",
                        highlightthickness=1, highlightbackground=BORDER)
        card.pack(fill="x", padx=24, pady=(18, 6))

        inner = tk.Frame(card, bg=CARD_BG, padx=20, pady=16)
        inner.pack(fill="x")
        inner.columnconfigure(1, weight=1)
        inner.columnconfigure(3, weight=1)

        # 과목
        tk.Label(inner, text="과목", font=(FONT, 10, "bold"),
                 bg=CARD_BG, fg=TEXT).grid(row=0, column=0, sticky="w", padx=(0, 8))
        self.subject_var = tk.StringVar()
        subject_cb = ttk.Combobox(inner, textvariable=self.subject_var,
                                   values=["(전체)"] + SUBJECTS,
                                   font=(FONT, 11), state="readonly", width=20)
        subject_cb.set("(전체)")
        subject_cb.grid(row=0, column=1, sticky="ew", padx=(0, 20))
        subject_cb.bind("<<ComboboxSelected>>", lambda e: self._search())

        # 성함
        tk.Label(inner, text="성함", font=(FONT, 10, "bold"),
                 bg=CARD_BG, fg=TEXT).grid(row=0, column=2, sticky="w", padx=(0, 8))
        self.name_var = tk.StringVar()
        name_entry = tk.Entry(inner, textvariable=self.name_var,
                              font=(FONT, 11), bd=1, relief="solid",
                              highlightthickness=1, highlightcolor=PRIMARY,
                              highlightbackground=BORDER, width=14)
        name_entry.grid(row=0, column=3, sticky="ew", padx=(0, 16))
        name_entry.bind("<KeyRelease>", lambda e: self._search())
        name_entry.bind("<Return>", lambda e: self._search())

        # 검색 버튼
        btn = tk.Button(inner, text="검 색", font=(FONT, 10, "bold"),
                        bg=PRIMARY, fg=BTN_FG, activebackground="#2a5ac8",
                        relief="flat", padx=14, pady=6, cursor="hand2",
                        command=self._search)
        btn.grid(row=0, column=4)

        # 초기화 버튼
        clr = tk.Button(inner, text="초기화", font=(FONT, 9),
                        bg=BG, fg=SUBTLE, activebackground=BORDER,
                        relief="flat", padx=8, pady=6, cursor="hand2",
                        command=self._reset)
        clr.grid(row=0, column=5, padx=(6, 0))

        # 결과 테이블
        result_frame = tk.Frame(self, bg=BG)
        result_frame.pack(fill="both", expand=True, padx=24, pady=(6, 16))

        # 헤더 행
        thead = tk.Frame(result_frame, bg=PRIMARY)
        thead.pack(fill="x")
        for col, w in [("과목", 18), ("성함", 10), ("위치", 20), ("근무요일", 18)]:
            tk.Label(thead, text=col, font=(FONT, 10, "bold"), bg=PRIMARY,
                     fg=BTN_FG, width=w, anchor="center", pady=8).pack(side="left")

        # 스크롤 영역
        wrap = tk.Frame(result_frame, bg=BORDER, bd=0)
        wrap.pack(fill="both", expand=True)

        canvas = tk.Canvas(wrap, bg=CARD_BG, bd=0, highlightthickness=0)
        vsb = ttk.Scrollbar(wrap, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=vsb.set)
        vsb.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        self.scroll_frame = tk.Frame(canvas, bg=CARD_BG)
        self._canvas_window = canvas.create_window((0, 0), window=self.scroll_frame,
                                                    anchor="nw")
        self.scroll_frame.bind("<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.bind("<Configure>",
            lambda e: canvas.itemconfig(self._canvas_window, width=e.width))
        canvas.bind_all("<MouseWheel>",
            lambda e: canvas.yview_scroll(-1 * (e.delta // 120), "units"))

        self.canvas = canvas

        # 상태 바
        self.status_var = tk.StringVar(value="")
        tk.Label(self, textvariable=self.status_var, font=(FONT, 9),
                 bg=BG, fg=SUBTLE, anchor="w").pack(fill="x", padx=24, pady=(0, 8))

        self._render_rows(df)

    # ── 검색 ─────────────────────────────────────────────
    def _search(self):
        subject = self.subject_var.get().strip()
        name    = self.name_var.get().strip()

        result = df.copy()
        if subject and subject != "(전체)":
            result = result[result["과목"] == subject]
        if name:
            result = result[result["성함"].str.contains(name, na=False)]

        self._render_rows(result)

    def _reset(self):
        self.subject_var.set("(전체)")
        self.name_var.set("")
        self._render_rows(df)

    # ── 행 렌더링 ─────────────────────────────────────────
    def _render_rows(self, data: pd.DataFrame):
        for w in self.scroll_frame.winfo_children():
            w.destroy()

        if data.empty:
            tk.Label(self.scroll_frame, text="검색 결과가 없습니다.",
                     font=(FONT, 11), bg=CARD_BG, fg=SUBTLE,
                     pady=30).pack()
            self.status_var.set("결과 없음")
            return

        COLS = [("과목", 18), ("성함", 10), ("위치", 20), ("근무요일", 18)]
        for i, (_, row) in enumerate(data.iterrows()):
            bg = ROW_ALT if i % 2 == 0 else CARD_BG
            r = tk.Frame(self.scroll_frame, bg=bg,
                         highlightthickness=0)
            r.pack(fill="x")
            for key, w in COLS:
                tk.Label(r, text=row[key], font=(FONT, 10),
                         bg=bg, fg=TEXT, width=w, anchor="center",
                         pady=9, wraplength=160).pack(side="left")
            # 구분선
            tk.Frame(self.scroll_frame, height=1, bg=BORDER).pack(fill="x")

        self.status_var.set(f"총 {len(data)}명 검색됨")
        self.canvas.yview_moveto(0)


if __name__ == "__main__":
    app = TeacherApp()
    app.mainloop()
