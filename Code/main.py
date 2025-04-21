import requests
import imgkit

dictionary={}
count=0
def html_to_image(html_content, output_filename):
    # Specify the path to wkhtmltoimage executable
    path_to_wkhtmltoimage = 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltoimage.exe'

    # Convert HTML to image using imgkit
    imgkit.from_string(html_content, output_filename, config=imgkit.config(wkhtmltoimage=path_to_wkhtmltoimage,))

    print(f"Image saved as {output_filename}")

def save_image_from_post_request(url, form_data):
    # Perform the POST request with form data
    headers={
        "Content-Type":"application/x-www-form-urlencoded",
        "Accept":"image/webp",
    }
    response = requests.post(url, data=form_data,headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        
        ind=response.text.index("<strong>/ 1400")
        sub=response.text[slice(ind-5,ind)]
        if sub not in dictionary:
            dictionary[sub]=[]
            dictionary[sub].append(response.text)
        else:
            dictionary[sub].append(response.text)

    else:
        print("Failed to retrieve image")


# Example usage
if __name__ == "__main__":
    url = "http://centres.muhs.edu.in/Vf$ato/JR/MX1/ug_res/W23/res_x119.asp"

    for i in range(211947,212190):
        form_data = {"cr": "MBBS-2019", "cl": "4", "sn": f"{i}"}
        save_image_from_post_request(url, form_data)

    # print(dictionary)
    keys=['1046 ', '1023 ', '0999 ', '0986 ', '0978 ', '0976 ', '0974 ', '0972 ', '0969 ', '0967 ', '0965 ', '0962 ', '0960 ', '0957 ', '0956 ', '0954 ', '0953 ', '0952 ', '0950 ', '0949 ', '0947 ', '0944 ', '0943 ', '0942 ', '0941 ', '0940 ', '0939 ', '0936 ', '0934 ', '0932 ', '0929 ', '0928 ', '0927 ', '0926 ', '0925 ', '0921 ', '0920 ', '0919 ', '0917 ', '0916 ', '0915 ', '0914 ', '0913 ', '0910 ', '0909 ', '0908 ', '0906 ', '0905 ', '0903 ', '0902 ', '0901 ', '0900 ', '0899 ', '0898 ', '0897 ', '0896 ', '0895 ', '0894 ', '0893 ', '0887 ', '0886 ', '0884 ', '0883 ', '0881 ', '0880 ', '0878 ', '0877 ', '0876 ', '0873 ', '0872 ', '0871 ', '0870 ', '0869 ', '0868 ', '0867 ', '0866 ', '0864 ', '0863 ', '0862 ', '0861 ', '0860 ', '0859 ', '0857 ', '0856 ', '0855 ', '0853 ', '0852 ', '0851 ', '0850 ', '0847 ', '0845 ', '0843 ', '0840 ', '0839 ', '0837 ', '0836 ', '0835 ', '0834 ', '0833 ', '0831 ', '0830 ', '0829 ', '0828 ', '0827 ', '0826 ', '0825 ', '0824 ', '0823 ', '0820 ', '0818 ', '0817 ', '0816 ', '0815 ', '0808 ', '0806 ', '0805 ', '0804 ', '0799 ', '0796 ', '0795 ', '0794 ', '0791 ', '0776 ']
    print(keys)
    for i in keys:
        for j in range(len(dictionary[i])):
            output_filename =f"{i}_{j}_result.png"
            html_to_image(dictionary[i][j],output_filename)
