import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
from operations import create_account, view_all_accounts, deposit_money, withdraw_money, check_balance
import threading
import os

class BankApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Bank Management System")
        self.geometry("1280x720")
        self.set_theme()
        
        self.image_references = {}
        self.image_path_base = os.path.join(os.path.dirname(__file__), "image_file")
        
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.pack(expand=True, fill="both")
        
        self.show_main_menu()

    def set_theme(self):
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def _load_and_display_image(self, parent_frame, image_filename):
        try:
            image_path = os.path.join(self.image_path_base, image_filename)
            pil_image = Image.open(image_path)
            
            resized_image = pil_image.resize((640, 720), Image.LANCZOS)

            ctk_image = ctk.CTkImage(
                light_image=resized_image,
                dark_image=resized_image,
                size=(640, 720)
            )
            self.image_references[image_filename] = ctk_image
            image_label = ctk.CTkLabel(parent_frame, image=ctk_image, text="")
            image_label.pack(expand=True, fill="both")

        except FileNotFoundError:
            label = ctk.CTkLabel(parent_frame, text=f"Image\n({image_filename})\nNot Found", font=("Times New Roman", 16, "bold"))
            label.pack(expand=True, fill="both")

    def show_main_menu(self):
        self.clear_frame()
        
        container_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        container_frame.pack(fill="both", expand=True, padx=0, pady=0)
        
        left_panel = ctk.CTkFrame(container_frame, fg_color="transparent", width=640, height=720)
        left_panel.pack(side="left", fill="both", expand=True, padx=(0, 0))
        
        right_panel = ctk.CTkFrame(container_frame, corner_radius=0, fg_color="#F0F0F0", width=640, height=720)
        right_panel.pack(side="right", fill="both", expand=True, padx=(0, 0))
        right_panel.pack_propagate(False)

        self._load_and_display_image(left_panel, "Main dashboard.jpg")

        try:
            logo_path = os.path.join(self.image_path_base, "LOGO.png")
            logo_image = Image.open(logo_path)
            logo_ctk = ctk.CTkImage(light_image=logo_image, dark_image=logo_image, size=(100, 100))
            self.image_references["LOGO.png"] = logo_ctk
            logo_label = ctk.CTkLabel(right_panel, image=logo_ctk, text="")
            logo_label.pack(pady=(40, 0))
        except FileNotFoundError:
            ctk.CTkLabel(right_panel, text="Logo Not Found", font=("Times New Roman", 12)).pack(pady=(40, 0))

        ctk.CTkLabel(right_panel, text="Bank Management System", font=("Times New Roman", 24, "bold"), text_color="#000000").pack(pady=(10, 20))
        
        self.buttons = [
            ("Create Account", self.show_create_account_form),
            ("View All Accounts", self.view_all_accounts),
            ("Deposit Money", self.show_deposit_form),
            ("Withdraw Money", self.show_withdraw_form),
            ("Check Balance", self.show_check_balance_form),
            ("Exit", self.destroy)
        ]

        for text, command in self.buttons:
            btn = ctk.CTkButton(right_panel, text=text, command=command, font=("Times New Roman", 16), height=50, corner_radius=8, fg_color="#007BFF", hover_color="#0022B8")
            btn.pack(fill="x", pady=10, padx=40)
        
    def show_create_account_form(self):
        self.clear_frame()
        
        container_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        container_frame.pack(fill="both", expand=True, padx=0, pady=0)
        
        left_panel = ctk.CTkFrame(container_frame, fg_color="transparent", width=640, height=720)
        left_panel.pack(side="left", fill="both", expand=True, padx=(0, 0))
        
        right_panel = ctk.CTkFrame(container_frame, corner_radius=0, fg_color="#F0F0F0", width=640, height=720)
        right_panel.pack(side="right", fill="both", expand=True, padx=(0, 0))
        right_panel.pack_propagate(False)

        self._load_and_display_image(left_panel, "create account.jpg")

        ctk.CTkLabel(right_panel, text="Create New Account", font=("Times New Roman", 20, "bold"), text_color="#333333").pack(pady=(20, 20))
        
        self.name_entry = self._create_input_field(right_panel, "Account Name:")
        self.email_entry = self._create_input_field(right_panel, "Account Email:")
        self.dob_entry = self._create_input_field(right_panel, "Date of Birth (YYYY-MM-DD):")
        self.address_entry = self._create_input_field(right_panel, "Present Address:")
        self.amount_entry = self._create_input_field(right_panel, "Initial Deposit Amount:")
        
        submit_btn = ctk.CTkButton(right_panel, text="Create Account", 
                               command=lambda: self._run_in_thread(
                                   create_account,
                                   self.show_main_menu,
                                   self.name_entry.get(),
                                   self.email_entry.get(),
                                   self.dob_entry.get(),
                                   self.address_entry.get(),
                                   self.amount_entry.get()
                               ), 
                               font=("Times New Roman", 14), height=40, corner_radius=8, fg_color="#007BFF", hover_color="#0022B8")
        submit_btn.pack(pady=20, padx=40, fill="x")
        
        self.create_back_button(right_panel)

    def view_all_accounts(self):
        self.clear_frame()
        
        container_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        container_frame.pack(fill="both", expand=True, padx=0, pady=0)
        
        left_panel = ctk.CTkFrame(container_frame, fg_color="transparent", width=640, height=720)
        left_panel.pack(side="left", fill="both", expand=True, padx=(0, 0))
        
        right_panel = ctk.CTkFrame(container_frame, corner_radius=0, fg_color="#F0F0F0", width=640, height=720)
        right_panel.pack(side="right", fill="both", expand=True, padx=(0, 0))
        right_panel.pack_propagate(False)

        self._load_and_display_image(left_panel, "view all bank accounts.jpg")

        ctk.CTkLabel(right_panel, text="All Accounts", font=("Times New Roman", 20, "bold"), text_color="#333333").pack(pady=(20, 20))

        table_frame = ctk.CTkScrollableFrame(right_panel, fg_color="transparent")
        table_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        headers = ["ID", "Name", "Email", "DOB", "Address", "Amount"]
        for col, header in enumerate(headers):
            label = ctk.CTkLabel(table_frame, text=header, font=("Times New Roman", 12, "bold"), padx=5, pady=5)
            label.grid(row=0, column=col, sticky="w", padx=5, pady=5)
        
        for i in range(len(headers)):
            table_frame.grid_columnconfigure(i, weight=1)

        def update_gui(accounts_data):
            if accounts_data:
                for row_idx, acc in enumerate(accounts_data):
                    for col_idx, data in enumerate(acc):
                        label = ctk.CTkLabel(table_frame, text=str(data), font=("Times New Roman", 12), padx=5, pady=2)
                        label.grid(row=row_idx + 1, column=col_idx, sticky="w", padx=5, pady=2)
            else:
                messagebox.showinfo("Operation Status", "No accounts found or an error occurred.")
            messagebox.showinfo("Operation Status", "View All Accounts completed.")

        def run_view_all():
            accounts_data = view_all_accounts()
            self.after(0, lambda: update_gui(accounts_data))

        threading.Thread(target=run_view_all).start()
        
        self.create_back_button(right_panel)

    def show_deposit_form(self):
        self.clear_frame()

        container_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        container_frame.pack(fill="both", expand=True, padx=0, pady=0)
        
        left_panel = ctk.CTkFrame(container_frame, fg_color="transparent", width=640, height=720)
        left_panel.pack(side="left", fill="both", expand=True, padx=(0, 0))
        
        right_panel = ctk.CTkFrame(container_frame, corner_radius=0, fg_color="#F0F0F0", width=640, height=720)
        right_panel.pack(side="right", fill="both", expand=True, padx=(0, 0))
        right_panel.pack_propagate(False)

        self._load_and_display_image(left_panel, "Deposit money.jpg")

        ctk.CTkLabel(right_panel, text="Deposit Money", font=("Times New Roman", 20, "bold"), text_color="#333333").pack(pady=(20, 20))

        self.account_id_entry = self._create_input_field(right_panel, "Account ID:")
        self.amount_entry = self._create_input_field(right_panel, "Deposit Amount:")

        submit_btn = ctk.CTkButton(right_panel, text="Deposit",
                               command=lambda: self._run_in_thread(
                                   deposit_money,
                                   self.show_main_menu,
                                   self.account_id_entry.get(),
                                   self.amount_entry.get()
                               ),
                               font=("Times New Roman", 14), height=40, corner_radius=8, fg_color="#007BFF", hover_color="#0022B8")
        submit_btn.pack(pady=20, padx=40, fill="x")

        self.create_back_button(right_panel)
        
    def show_withdraw_form(self):
        self.clear_frame()

        container_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        container_frame.pack(fill="both", expand=True, padx=0, pady=0)
        
        left_panel = ctk.CTkFrame(container_frame, fg_color="transparent", width=640, height=720)
        left_panel.pack(side="left", fill="both", expand=True, padx=(0, 0))
        
        right_panel = ctk.CTkFrame(container_frame, corner_radius=0, fg_color="#F0F0F0", width=640, height=720)
        right_panel.pack(side="right", fill="both", expand=True, padx=(0, 0))
        right_panel.pack_propagate(False)

        self._load_and_display_image(left_panel, "withdraw money.jpg")

        ctk.CTkLabel(right_panel, text="Withdraw Money", font=("Times New Roman", 20, "bold"), text_color="#333333").pack(pady=(20, 20))

        self.account_id_entry = self._create_input_field(right_panel, "Account ID:")
        self.amount_entry = self._create_input_field(right_panel, "Withdraw Amount:")

        submit_btn = ctk.CTkButton(right_panel, text="Withdraw",
                               command=lambda: self._run_in_thread(
                                   withdraw_money,
                                   self.show_main_menu,
                                   self.account_id_entry.get(),
                                   self.amount_entry.get()
                               ),
                               font=("Times New Roman", 14), height=40, corner_radius=8, fg_color="#007BFF", hover_color="#0022B8")
        submit_btn.pack(pady=20, padx=40, fill="x")

        self.create_back_button(right_panel)

    def show_check_balance_form(self):
        self.clear_frame()

        container_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        container_frame.pack(fill="both", expand=True, padx=0, pady=0)
        
        left_panel = ctk.CTkFrame(container_frame, fg_color="transparent", width=640, height=720)
        left_panel.pack(side="left", fill="both", expand=True, padx=(0, 0))
        
        right_panel = ctk.CTkFrame(container_frame, corner_radius=0, fg_color="#F0F0F0", width=640, height=720)
        right_panel.pack(side="right", fill="both", expand=True, padx=(0, 0))
        right_panel.pack_propagate(False)

        self._load_and_display_image(left_panel, "check balance.jpg")

        ctk.CTkLabel(right_panel, text="Check Balance", font=("Times New Roman", 20, "bold"), text_color="#000000").pack(pady=(20, 20))

        self.account_id_entry = self._create_input_field(right_panel, "Account ID:")

        submit_btn = ctk.CTkButton(right_panel, text="Check Balance",
                               command=lambda: self._run_in_thread(
                                   check_balance,
                                   None,
                                   self.account_id_entry.get()
                               ),
                               font=("Times New Roman", 14), height=40, corner_radius=8, fg_color="#007BFF", hover_color="#0022B8")
        submit_btn.pack(pady=20, padx=40, fill="x")

        self.create_back_button(right_panel)
    
    def create_back_button(self, parent_frame):
        back_btn = ctk.CTkButton(parent_frame, text="Back to Main Menu", command=self.show_main_menu, font=("Times New Roman", 13), fg_color="#008300", hover_color="#A00000", width=200, corner_radius=8)
        back_btn.pack(pady=(30, 0), padx=40)
    
    def _create_input_field(self, parent_frame, label_text):
        frame = ctk.CTkFrame(parent_frame, fg_color="transparent")
        frame.pack(fill="x", pady=5, padx=40)
        ctk.CTkLabel(frame, text=label_text, font=("Times New Roman", 12), text_color="#333333").pack(anchor="w", pady=(0, 5))
        entry = ctk.CTkEntry(frame, font=("Times New Roman", 12), placeholder_text=label_text.replace(":", ""), corner_radius=8)
        entry.pack(fill="x")
        return entry

    def _run_in_thread(self, func, success_callback=None, *args):
        def run_operation():
            try:
                result_message = func(*args)
                if result_message is not None:
                    self.after(0, lambda: messagebox.showinfo("Operation Status", result_message))
                    if success_callback:
                        self.after(0, success_callback)
            except Exception as e:
                self.after(0, lambda: messagebox.showerror("Error", f"An error occurred: {e}"))
                self.after(0, self.show_main_menu)
        threading.Thread(target=run_operation).start()

if __name__ == "__main__":
    app = BankApp()
    app.mainloop()
