try:
    import speedtest as s #pip install speedtest
    from speak import speak

    def check_internet_speed():
        speak('Sir, I am checking your internet speed. This may take a while, Please wait') 
        st = s.Speedtest()
        dl = st.download()
        dl1 = round(float(float(dl)/800000),2)
        up = st.upload()
        up1 = round(float(float(up)/800000),2)
        speak(f'your uploading speed is approximately {up1} Mb per second')
        speak(f'and your downloading speed is approximately {dl1} Mb per second')

except Exception as e:print(e)