import streamlit as st
class Bank:
    balance = 50000

    def deposit(self):
        amount = st.number_input("enter amount to deposit:")
        #if amount:
        if (amount < 100 or amount > 50000):
            st.warning("Minimum deposit is 100 and Maximum deposit is 50000")
        elif (amount % 100 == 0):
            self.balance = self.balance + amount
            st.title(f"{amount} is deposited ")
            self.bal_enquiry()
            st.text("************Transaction successful*********")
        else:
            st.warning("amount should be in multiples of 100")

    def withdraw(self):
       amount = st.number_input("enter amount to withdraw:")
       min_bal=500
       minacc=self.balance-min_bal
       #if amount:
       if (amount < 100 or amount > minacc):
           st.warning(
               f"Minimum withdrawl is 100 and Maximum withdrawal is {minacc} as there should be a minimum balance of 500 in your acc")
       elif (amount % 100 == 0):
           self.balance = self.balance - amount
           st.title(f"{amount} is withdrawn ")
           self.bal_enquiry()
           st.text("************Transaction successful*********")
       else:
           st.warning("amount should be in multiples of 100")

    def bal_enquiry(self):
        st.title(f"balance:{self.balance}")

    def viewoptions(self):
        transac=3
        while(transac>0):
            st.text("----------------Transaction---------------------")
            if st.button("1.Deposit"):
                self.deposit()
            elif st.button("2.withdraw"):
                self.withdraw()
            elif st.button("3.Bal Enquiry"):
                self.bal_enquiry()
            elif st.button("4.Exit"):
                exit()
            #else:
                #st.text("invalid option .....")
            transac=transac-1



    def validate(self):
        chance = 3
        while (chance > 0):
            pin = st.text_input("enter your pin:")
            actual_pin = "1234"
            if pin:
                if (pin == actual_pin):
                    self.viewoptions()
                    break
                else:
                    if (chance == 1):
                        st.text("your card is blocked...")
                    else:
                        st.text("incorrect pin try again...")
                chance = chance - 1



obj = Bank()
obj.validate()