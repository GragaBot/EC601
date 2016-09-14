
# coding: utf-8
//hi

# In[10]:

# AUTHOR ZITENG XU zxu83@bu.edu
import math;
earth_mass = 5.98*(10**24)
earth_molar_mass = (55.845*32.1/100) + (15.9994*30.1/100) + (28.0855*15.1/100) + (24.3050*13.9/100) + (32.065 * 2.9/100)+(58.6934 *1.8/100) + (40.078 *1.5/100) + (26.9815*1.4/100)
#molar mass of earth (Fe, O, Si Mg, S, Ni, Ca, Al)

electron_per_molar = 26 + 8 +14 +12 + 16 + 28 + 20 +13;

molar_earth = earth_mass / earth_molar_mass;
aov_number = 6.022 * (10 **23)
total_electron = electron_per_molar * molar_earth * aov_number / (10**12);

print (total_electron)



lower_earth_molar_mass = (55.845*32.1/100) + (15.9994*30.1/100) + (28.0855*15.1/100) + (24.3050*13.9/100) +(58.6934 *1.8/100) + (40.078 *1.5/100) + (26.9815*1.4/100);
#molar mass of earth (Fe, O, Si Mg, Ni, Ca, Al)
lower_electron_per_molar = 26 + 8 +14 +12 + 28 + 20 +13;
    
lower_molar_earth = earth_mass / lower_earth_molar_mass;
lower_total_electron = lower_electron_per_molar * lower_molar_earth * aov_number / (10**12);
print(lower_total_electron)
print((lower_total_electron + total_electron)/2);



# In[ ]:



