import geopandas
import matplotlib.pyplot as plt
import re

# Use a font that supports Chinese characters
# We could learn how to do this by asking Gemini 
# "set the default font in matplotlib to one that supports Chinese characters"
# The SimSun font is present on most Windows systems.  For non-Windows systems, 
# you might need something else.
plt.rcParams["font.family"] = "SimSun"
china = geopandas.read_file('../data/maps/china_provinces.json')

china['label'] = ''
china['long_name'] = ''

# Add a column with the position of the label
# The representative_point() method tries to return an appropriate point for
# the label even if the region has a strange, highly non-convex shape.
china['label_pos'] = china['geometry'].apply(lambda x: [* x.representative_point().coords[0]])

# loop over rows
labels = []
for idx, x in china.iterrows():
    # The next line is usually the same as n = x['NAME_1'] but we add some extra code
    # to insert spaces where needed, which converts 'HongKong' to 'Hong Kong' and
    # 'NingxiaHui' to 'Ningxia Hui'.  In more detail, the regular expression
    # '([A-Z]+)' matches any sequence of capital letters.  The expression r' \1'
    # means "a space followed by the thing that was matched", so it inserts a space
    # before each capital letter.  In particular it will usually insert a space 
    # right at the beginning of the string, so we use strip() to remove it.
    n = re.sub('([A-Z]+)', r' \1', x['NAME_1']).strip()
    # We have some special cases for Hong Kong and Macau
    if x['NAME_1'] == 'HongKong':
        s = '香港'
        n = 'the Hong Kong SAR'
    elif x['NAME_1'] == 'Macau':
        s = '澳门'
        n = 'the Macao SAR'
    else:
        # If there is a bar in the name, we use the part after the bar
        # If there is no bar, we use the whole name
        s = x['NL_NAME_1'].split('|')[-1]
        # Remove the last three characters if they are '自治区'
        # (meaning 'autonomous region').  Chinese-speaking students can comment
        # on whether it would be appropriate to remove '族' as well leaving 
        # '宁夏回' instead of '宁夏回族' and '广西壮' instead of '广西壮族'.
        if s[-3:] == '自治区':
            s = s[:-3]
        if x['ENGTYPE_1'] == 'Province':
            n = 'the province of ' + n
        elif x['ENGTYPE_1'] == 'Municipality':
            n = 'the city of ' + n
        elif x['ENGTYPE_1'] == 'AutonomousRegion':
            n = 'the ' + n + ' Autonomous Region '
    if s in labels:
        # If we get here, then the relevant region has several pieces, and we 
        # already have a label for the first piece.  Subsequent pieces are 
        # always much smaller and we do not label them.
        s = ''
    else:
        labels.append(s)
    # Note that slightly strange syntax is needed to assign to a cell in a
    # dataframe.  
    china.at[idx, 'label'] = s
    china.at[idx, 'long_name'] = n

def shift_label_pos(region, dx, dy):
    # Find the line number of the row with the given region
    i = china.loc[china['NAME_1'] == region].index[0]
    # Add dx and dy to the coordinates of the label
    v = china.at[i, 'label_pos']
    w = [v[0] + dx, v[1] + dy]
    china.at[i, 'label_pos'] = w

shift_label_pos('HongKong', 1, -1)
shift_label_pos('Macau',   -1, -1)
shift_label_pos('Hebei',    0, -1)

def show_region(region):
    """
    Plot the map of China with the specified region highlighted.  The region
    can be specified in English or Chinese, and it is not case-sensitive.
    """
    r = china.loc[china['NAME_1'].str.lower() == region.lower()]
    if len(r) == 0:
        r = china.loc[china['VARNAME_1'].str.lower() == region.lower()]
    if len(r) == 0:
        r = china.loc[china['label'].str.lower() == region.lower()]
    if len(r) == 0:
        raise ValueError(f'No region named {region}')
    fig, ax = plt.subplots(1, 1, figsize=(20, 10))
    ax.axis('off')
    ax.set_title('Map of China with ' + r['long_name'].values[0] + ' (' + r['label'].values[0] + ') highlighted')
    # Plot all the regions in light grey
    china.plot(edgecolor='darkgrey', facecolor='lightgrey', ax=ax)
    # Plot the selected region in light blue
    r.plot(facecolor='#9999ff', ax=ax)
    # Add text labels to all regions
    china.apply(lambda x: ax.annotate(text=x['label'], xy=x['label_pos'], ha='center'), axis=1)

show_region('Heilongjiang')
